from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI(title="Notifications Service")

class Notification(BaseModel):
    message: str

@app.post("/notify")
def notify(notification: Notification):
    print(f"[{datetime.datetime.now()}] {notification.message}")
    return {"status": "ok"}
