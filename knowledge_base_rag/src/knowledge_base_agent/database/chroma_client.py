import os
import chromadb
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

os.makedirs("db", exist_ok=True)

db_client = chromadb.PersistentClient(path="db")

def get_embedding_function():
    embedding_model = os.environ.get("EMBEDDING_MODEL", "text-embedding-3-large")
    return OpenAIEmbeddings(model=embedding_model)

embedding_function = get_embedding_function()

VECTOR_STORE_COLLECTION_NAME = "knowledge_base_agent_collection"


def create_vector_store() -> Chroma:
    return Chroma(
        embedding_function=embedding_function,
        collection_name=VECTOR_STORE_COLLECTION_NAME,
        client=db_client,
    )
