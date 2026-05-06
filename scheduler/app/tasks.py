from app.celery_app import celery_app
from datetime import datetime
import redis
from app.service import message_service 
from app.models.patient_message import PatientMessage
from typing import List

redis_client = redis.Redis(host="localhost", port=6379, db=0)
def get_message():
    patient_message_dict : List[PatientMessage]  =  message_service.get_message()
    return patient_message_dict
    """return f"Hello from Celery! Time: {datetime.now().strftime('%H:%M:%S')}"  """




@celery_app.task(name="app.tasks.send_message")
def send_message():
    patient_messages = get_message()
    patient_message_list = [PatientMessage(**d) for d in patient_messages]
    for message_list in patient_message_list:
        message = f"Time: {datetime.now().strftime('%H:%M:%S \n')}{ message_list.patient_message }"
        redis_client.publish(f"sse_channel_{message_list.patient_id}", message)


 

