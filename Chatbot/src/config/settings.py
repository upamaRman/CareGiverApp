from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass
class Config:
    """Application configuration."""
    pinecone_api_key: str
    pinecone_index_name: str
    openai_api_key: str
    embedding_model: str = "text-embedding-3-small"
    llm_model: str = "gpt-4o-mini"
    llm_temperature: float = 1.0
    retriever_k: int = 3
    retriever_score_threshold: float = 0.5

def load_config() -> Config:
    """Load configuration from environment variables."""
    load_dotenv()
    return Config(
        pinecone_api_key=os.environ["PINECONE_API_KEY"],
        pinecone_index_name=os.environ["PINECONE_INDEX_NAME"],
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )