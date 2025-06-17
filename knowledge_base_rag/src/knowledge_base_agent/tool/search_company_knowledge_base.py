from langchain_core.documents import Document

from src.knowledge_base_agent.database.chroma_client import create_vector_store


def search_company_knowledge_base(search: str) -> list[Document]:
    return create_vector_store().similarity_search(search, k=3)
