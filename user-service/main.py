from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI(title="Users Service")

users = {}

class User(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: User):
    user_id = str(uuid.uuid4())
    users[user_id] = user.dict()
    return {"id": user_id, "user": user}

@app.get("/users")
def list_users():
    return users
