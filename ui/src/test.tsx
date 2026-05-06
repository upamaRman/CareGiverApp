
import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState<string>("Waiting for message...");

  useEffect(() => {
    const eventSource = new EventSource("http://127.0.0.1:8000/events");
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
  }, []);

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h2>Live Message from Backend</h2>
      <div style={{ border: "1px solid #ccc", padding: "1rem", borderRadius: "8px" }}>
        {message}
      </div>
    </div>
  );
}

export default App;
