import React, { useState } from "react";

const FileUpload: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]);
    }
  };

  const uploadFile = async () => {
    if (!file) {
      alert("Please choose a file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://localhost:8003/upload-medication-image", {
      method: "POST",
      body: formData,
    });

    alert("File uploaded");
  };

  return (
    <div style={{ marginTop: "30px" }}>
      <h3>Upload Medication Image</h3>

      <input type="file" onChange={handleFileChange} />

      <br />
      <br />

      <button onClick={uploadFile}>Upload</button>
    </div>
  );
};

export default FileUpload;