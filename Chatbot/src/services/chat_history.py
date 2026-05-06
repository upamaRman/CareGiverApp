from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import streamlit as st

class ChatHistory:
    """Manages chat history in Streamlit session state."""
    
    def __init__(self):
        if "messages" not in st.session_state:
            st.session_state.messages = [SystemMessage("You are an assistant for question-answering tasks.")]
    
    def get_history(self) -> list:
        """Retrieve the current chat history."""
        return st.session_state.messages
    
    def add_message(self, message):
        """Add a message to the chat history."""
        st.session_state.messages.append(message)
    
    def display_history(self):
        """Display chat history in Streamlit."""
        for message in self.get_history():
            if isinstance(message, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant"):
                    st.markdown(message.content)