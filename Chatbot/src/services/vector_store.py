from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from src.config.settings import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VectorStoreService:
    """Manages Pinecone vector store operations."""
    
    def __init__(self, config: Config):
        self.config = config
        self.pc = Pinecone(api_key=config.pinecone_api_key)
        self.index = self.pc.Index(config.pinecone_index_name)
        self.embeddings = OpenAIEmbeddings(
            model=config.embedding_model,
            api_key=config.openai_api_key
        )
        self.vector_store = PineconeVectorStore(index=self.index, embedding=self.embeddings)

    def get_retriever(self):
        try:
            return self.vector_store.as_retriever(
                search_type = "similarity_score_threshold",
                search_kwargs = {
                    "k" : self.config.retriever_k,
                    "score_threshold": self.config.retriever_score_threshold
                }
            )
        except Exception as e:
            logger.error(f"Error creating retriever : {e}")
            raise
