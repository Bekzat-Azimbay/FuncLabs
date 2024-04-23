# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from myapp.tasks import process_event

class EventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Dispatch Celery task to handle the event asynchronously
        process_event.delay(data)
#dsxdcfyvbnm,