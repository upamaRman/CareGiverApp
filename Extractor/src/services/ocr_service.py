from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from src.config.settings import Config


class OCRService:
    def __init__(self, config: Config):
        self.client = DocumentIntelligenceClient(
            endpoint=config.azure_doc_endpoint,
            credential=AzureKeyCredential(config.azure_doc_key)
        )

    def extract_text_from_image(self, image_bytes: bytes) -> str:
        poller = self.client.begin_analyze_document(
            model_id="prebuilt-read",
            body=image_bytes
        )

        result = poller.result()

        lines = []

        for page in result.pages:
            for line in page.lines:
                lines.append(line.content)

        return "\n".join(lines)