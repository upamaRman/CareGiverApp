from openai import OpenAI
from src.schemas.patient_schema import Patient
from src.config.settings import Config


class ExtractService:
    def __init__(self, config: Config):
        self.client = OpenAI(api_key=config.openai_api_key)
        self.model = config.llm_model

        self.SYSTEM_PROMPT = """
You receive OCR text from an uploaded image.

Step 1:
Determine whether the text comes from a pharmacy medication receipt
or medication instruction sheet.

If NOT, respond with:
NOT_A_PHARMACY_DOC

Step 2:
If YES, extract medication information and return VALID JSON only.

Required JSON schema:
{
  "first_name": string | null,
  "last_name": string | null,
  "gender": string | null,
  "dob": date | null,
  "status": string | null,
  "medications": [
    {
      "medicine_name": string,
      "dosage": string | null,
      "frequency_per_day": int | null,
      "prescribed_date" : date | null,
      "instruction" : string | null,
      "status" : string | null,        
      "duration_days": int | null
    }
  ]
}
"""

    def extract_medication_data(self, ocr_text: str) -> Patient:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": ocr_text}
            ],
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        print(f"\n\n\nContent coming from chatgpt llm:  \n\n {content}")
        if content is None:
            raise ValueError("Empty response from LLM")

        if "NOT_A_PHARMACY_DOC" in content:
            print("*******NOT_A_PHARMACY_DOC")
            raise ValueError("Not a pharmacy document")

        print(f"\n\n\nContent before validation:  \n\n {content}")
        return Patient.model_validate_json(content)
