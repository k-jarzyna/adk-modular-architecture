from datetime import datetime
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.knowledge_base_agent.database.chroma_client import create_vector_store

MIN_CONTENT_LENGTH = 50
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200

def import_document(content: str) -> str:
    if not content or len(content.strip()) < MIN_CONTENT_LENGTH:
        return "Content too short or empty. Please provide more detailed information."
        
    content_split = RecursiveCharacterTextSplitter(
        chunk_size=DEFAULT_CHUNK_SIZE, chunk_overlap=DEFAULT_CHUNK_OVERLAP
    ).split_text(content)
    source = "unknown"
    metadatas = [{"source": source, "date_added": datetime.now().isoformat()} for _ in content_split]
    
    create_vector_store().add_texts(texts=content_split, metadatas=metadatas)
    return f"Successfully imported {len(content_split)} chunks of content."
