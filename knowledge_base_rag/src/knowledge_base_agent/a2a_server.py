import os
import sys

from dotenv import load_dotenv

load_dotenv()
import ssl
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

from agent import root_agent
from google.adk import Agent, Runner
from google.adk.agents.invocation_context import InvocationContext, new_invocation_context_id, Session
from google.adk.agents import LiveRequestQueue, RunConfig
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory import InMemoryMemoryService
from google.adk.sessions import InMemorySessionService
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
    DataPart,   
    InvalidParamsError,
    SendStreamingMessageSuccessResponse,
    Task,
    TaskArtifactUpdateEvent,
    TaskState,
    TaskStatusUpdateEvent,
    TextPart,
    UnsupportedOperationError,
)
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message, new_task
from a2a.server.tasks import TaskUpdater
from a2a.utils.errors import ServerError
from google.adk.agents import BaseAgent

import uvicorn
from google.genai.types import Part, Content, Modality

import uuid

from typing import AsyncGenerator

from google.adk.agents import Agent
from google.adk.events import Event
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types


class AgentRunner:
    def __init__(
        self,
        user_id: str = 'user_1',
        app_name: str = 'A2A',
    ):
        self.session_service = InMemorySessionService()
        self.session = None
        self.app_name = app_name
        self.user_id = user_id

    async def run_stream(
        self, agent: Agent, query: str, session_id: str
    ) -> AsyncGenerator[Event, None]:
        runner = Runner(
            agent=agent,
            app_name=self.app_name,
            session_service=self.session_service,
        )
        if not session_id:
            session_id = uuid.uuid4().hex
        else:
            self.session = self.session_service.get_session(
                app_name=self.app_name,
                user_id=self.user_id,
                session_id=session_id,
            )
        if not self.session:
            self.session = self.session_service.create_session(
                app_name=self.app_name,
                user_id=self.user_id,
                session_id=session_id,
            )
        content = types.Content(role='user', parts=[types.Part(text=query)])

        async for event in runner.run_async(
            user_id=self.user_id,
            session_id=self.session.id,
            new_message=content,
        ):
            if event.is_final_response():
                response = ''
                if (
                    event.content
                    and event.content.parts
                    and event.content.parts[0].text
                ):
                    response = '\n'.join(
                        [p.text for p in event.content.parts if p.text]
                    )
                elif (
                    event.content
                    and event.content.parts
                    and any(
                        True for p in event.content.parts if p.function_response
                    )
                ):
                    response = next(
                        p.function_response.model_dump()
                        for p in event.content.parts
                    )
                else:
                    response = f'Error in running agent: {agent.name}'
                yield {
                    'type': 'final_result',
                    'response': response,
                }
            else:
                yield {
                    'is_task_complete': False,
                    'require_user_input': False,
                    'content': f'{agent.name}: Processing request...',
                }

class MyAgentExecutor(AgentExecutor):
    def __init__(self, agent: BaseAgent):
        self.agent = agent

    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        error = self._validate_request(context)
        if error:
            raise ServerError(error=InvalidParamsError())

        query = context.get_user_input()

        task = context.current_task

        if not task:
            task = new_task(context.message)
            event_queue.enqueue_event(task)

        updater = TaskUpdater(event_queue, task.id, task.contextId)
        runner = AgentRunner()

        async for item in runner.run_stream(self.agent, query, task.contextId):
            if hasattr(item, 'root') and isinstance(
                item.root, SendStreamingMessageSuccessResponse
            ):
                event = item.root.result
                if isinstance(
                    event,
                    (TaskStatusUpdateEvent | TaskArtifactUpdateEvent),
                ):
                    event_queue.enqueue_event(event)
                continue

            import json
            is_task_complete = item.get('type', False)
            require_user_input = item['require_user_input'] if hasattr(item, 'require_user_input') else False

            if is_task_complete == 'final_result':
                updater.complete(
                    message = new_agent_text_message(
                        item.get('response', 'No respnse'),
                        task.contextId,
                        task.id,
                    ),
                )
                break
            else:
                updater.update_status(
                    TaskState.working,
                    new_agent_text_message(
                        f'Processing request...',
                        task.contextId,
                        task.id,
                    ),
                )

    def _validate_request(self, context: RequestContext) -> bool:
        return False


    async def cancel(
        self, request: RequestContext, event_queue: EventQueue
    ) -> Task | None:
        raise ServerError(error=UnsupportedOperationError())

def main():
    try:
        port = int(os.environ.get("A2A_SERVER_PORT"))
        host = os.environ.get("A2A_SERVER_HOST")
        protocol = os.environ.get("A2A_SERVER_PROTOCOL")

        capabilities = AgentCapabilities(
            streaming=True,
        )
        skill = AgentSkill(
            id="company_knowledge_search",
            name="Company knowledge search",
            description="Agent skill to find previous company experience and projects.",
            tags=["search"],
            examples=[
                "Could you tell me about the company experience with Python projects, AI and ML?"
            ],
        )
        agent_card = AgentCard(
            name="Knowledge Base Agent",
            description="This agent handles requests about the "
            "software company experience and previous projects.",
            url=f"{protocol}://{host}:{port}/",
            version="1.0.0",
            defaultInputModes=["stream"],
            defaultOutputModes=["stream"],
            capabilities=capabilities,
            skills=[skill],
        )

        request_handler = DefaultRequestHandler(
                agent_executor=MyAgentExecutor(agent=root_agent),
                task_store=InMemoryTaskStore(),
            )

        server = A2AStarletteApplication(
            agent_card=agent_card,
            http_handler=request_handler
        )

        uvicorn.run(server.build(), host=host, port=port)
    except Exception as e:
        print(e)


main()
