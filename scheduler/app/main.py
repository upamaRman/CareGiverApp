from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse
import redis
import asyncio
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

async def event_generator(patient_id: int):
    pubsub = redis_client.pubsub()
    channel = f"sse_channel_{patient_id}"
    pubsub.subscribe(channel)

    try:
        while True:
            message = pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
            if message:
                yield {
                    "event": "message",
                    "data": message["data"]
                }
            await asyncio.sleep(0.1)
    finally:
        pubsub.close()   

@app.get("/sse/{patient_id}")
async def sse_endpoint(patient_id: int):
    return EventSourceResponse(event_generator(patient_id))

