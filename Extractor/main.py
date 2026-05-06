from fastapi import FastAPI, UploadFile, File, HTTPException,  BackgroundTasks
from fastapi.encoders import jsonable_encoder
from src.services.ocr_service import OCRService
from src.services.extract_service import ExtractService
from src.services.api_client_service import APIClient
from src.config.settings import load_config

app = FastAPI()

async def send_result_to_api(result: dict, endpoint: str):
    api_client = APIClient(endpoint)
    # convert pydantic model / datetime / etc to JSON-safe
    result_json = jsonable_encoder(result)

    await api_client.send_data(result_json)


@app.post("/upload-medication-image")
async def upload_medication_image(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    config = load_config()

    ocr_service = OCRService(config)
    extract_service = ExtractService(config)

    image_bytes = await file.read()

    try:
        ocr_text = ocr_service.extract_text_from_image(image_bytes)
        print(ocr_text)
        result = extract_service.extract_medication_data(ocr_text)
        print(f"\n\n\nResult::::::  \n\n {result}")

        background_tasks.add_task(
            send_result_to_api,
            result,
            config.medical_data_save_endpoint
        )        
        return {
            "status": "success",
            "data": result
        }

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Image is not a pharmacy medication document"
        )