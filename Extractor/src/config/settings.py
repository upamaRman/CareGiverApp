from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass
class Config:
    """Application configuration."""
    openai_api_key: str
    azure_doc_endpoint : str
    azure_doc_key : str
    medical_data_save_endpoint : str
    embedding_model: str 
    llm_model: str 

def load_config() -> Config:
    """Load configuration from environment variables."""
    load_dotenv()
    return Config(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        azure_doc_endpoint=os.getenv("AZURE_DOC_ENDPOINT"),
        azure_doc_key=os.getenv("AZURE_DOC_KEY"),
        medical_data_save_endpoint = os.getenv("MEDICAL_DATA_SAVE_ENDPOINT"),
        llm_model=os.getenv("LLM_MODEL"),
        embedding_model = os.getenv("EMBEDDING_MODEL")
    )