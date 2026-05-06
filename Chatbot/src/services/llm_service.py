from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from src.config.settings import Config
import logging

logger = logging.getLogger(__name__)

class LLMService:
    """Manages LLM interactions."""
    
    def __init__(self, config: Config):
        self.config = config
        self.llm = ChatOpenAI(
            model=config.llm_model,
            temperature=config.llm_temperature,
            api_key=config.openai_api_key
        )
        self.system_prompt_template = """You are an assistant for question-answering tasks. 
        Use the following pieces of retrieved context to answer the question. 
        If you don't know the answer, just say that you don't know. 
        Use three sentences maximum and keep the answer concise.
        Context: {context}"""

    def generate_response(self, prompt: str, retriever, chat_history: list) -> str:
        """Generate a response for the given prompt."""
        try:
            docs = retriever.invoke(prompt)
            docs_text = "".join(d.page_content for d in docs)
            system_prompt = self.system_prompt_template.format(context=docs_text)
            
            # Update chat history
            chat_history.append(SystemMessage(system_prompt))
            chat_history.append(HumanMessage(prompt))
            
            # Generate response
            response = self.llm.invoke(chat_history).content
            chat_history.append(AIMessage(response))
            return response
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "Sorry, an error occurred while processing your request."