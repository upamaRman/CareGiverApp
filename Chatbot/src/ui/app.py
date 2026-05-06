import streamlit as st
from src.config.settings import load_config
from src.services.vector_store import VectorStoreService
from src.services.llm_service import LLMService
from src.services.chat_history import ChatHistory

def main():
    # st.title("Chatbot")
    
    # Load configuration
    config = load_config()
    
    # Initialize services
    vector_store_service = VectorStoreService(config)
    llm_service = LLMService(config)
    chat_history = ChatHistory()
    
    # Display chat history
    chat_history.display_history()
    
    # Handle user input
    if prompt := st.chat_input("How can I assist you?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display response
        retriever = vector_store_service.get_retriever()
        response = llm_service.generate_response(
            prompt=prompt,
            retriever=retriever,
            chat_history=chat_history.get_history()
        )
        
        with st.chat_message("assistant"):
            st.markdown(response)

if __name__ == "__main__":
    main()