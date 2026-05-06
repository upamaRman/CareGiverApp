import React, { useEffect, useState } from "react";
import FileUpload from "./FileUpload";
import StreamlitChatbot from "./StreamlitChatbot";

interface AppProps {
  patientId: string;
}

const App: React.FC<AppProps> = ({ patientId }) => {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const eventSource = new EventSource(
      `http://localhost:8000/sse/${patientId}`
    );

    eventSource.onmessage = (event) => {
      setMessage(event.data);
    };

    eventSource.onerror = () => {
      console.error("SSE connection error");
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, [patientId]);

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <pre>    <FileUpload />  </pre>
      <br/>
      <br/>
      <br/>
      <h3>Server-Sent Notification for patients</h3>
      <pre>{message}</pre>

     {/* ✅ Add chatbot here */}
      <StreamlitChatbot />
    </div>
  );
};

export default App;





/* import React, { useEffect, useState } from "react";


interface AppProps {
  patientId: string; // pass the patient id here
}

const App: React.FC<AppProps> = ({ patientId }) => {

  const [message, setMessage] = useState("");

  useEffect(() => {
    const eventSource = new EventSource("http://localhost:8000/sse/4");

    eventSource.onmessage = (event) => {
      setMessage(event.data);
    };

    eventSource.onerror = () => {
      console.error("SSE connection error");
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, [patientId]);

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Server-Sent Notification for patients</h1>
      <p>{message}</p>
    </div>
  );
};

export default App;
*/