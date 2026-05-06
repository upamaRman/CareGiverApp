const StreamlitChatbot: React.FC = () => {
    return (
      <div style={{ marginTop: "2rem" }}>
        <h3>Chatbot</h3>
  
        <iframe
          src="http://localhost:8501" // your Streamlit URL
          title="Streamlit Chatbot"
          width="100%"
          height="600px"
          style={{
            border: "1px solid #ccc",
            borderRadius: "8px",
          }}
        />
      </div>
    );
  };
  
  export default StreamlitChatbot;