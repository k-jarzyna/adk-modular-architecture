import os
import sys


from typing import override, AsyncGenerator
from uuid import uuid4
from typing import Any

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.genai.types import Content, Part
import httpx

from a2a.client import A2ACardResolver, A2AClient
from a2a.types import (
    MessageSendParams,
    SendStreamingMessageRequest
)

async def fetch_remote_agent(httpx_client: httpx.AsyncClient):
    PUBLIC_AGENT_CARD_PATH = '/.well-known/agent.json'
    base_url = os.environ.get("KNOWLEDGE_BASE_A2A_URL")

    resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=base_url,
        )
    _public_card = await resolver.get_agent_card()

    return _public_card

class RemoteAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(
            name=name
        )

    @override
    async def _run_async_impl(
            self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        async with httpx.AsyncClient() as httpx_client:
            import json
            agent_card = await fetch_remote_agent(httpx_client)
            client = A2AClient(
                httpx_client=httpx_client, agent_card=agent_card
            )
            send_message_payload: dict[str, Any] = {
                'message': {
                    'role': 'user',
                    'parts': [
                        {'kind': 'text', 'text': ctx.session.events[0].content.parts[0].text}
                    ],
                    'messageId': uuid4().hex,
                },
            }
            request = SendStreamingMessageRequest(
                id=str(uuid4()), params=MessageSendParams(**send_message_payload)
            )

            response = client.send_message_streaming(request)
            
            async for event in response:
                print(f"Received event: {event}")            
            if hasattr(event, 'root') and hasattr(event.root, 'result') and event.root.result.final:
                yield Event(
                        author=self.name,
                        content=Content(
                            parts=[
                                Part(
                                    text=event.root.result.status.message.parts[0].root.text
                                )
                            ]
                        )
                    )

knowledge_base_remote_agent = RemoteAgent(
    name="knowledge_base_remote_agent"
)
