from typing import Optional, List
from fastapi import FastAPI, Path

from pydantic import BaseModel

app = FastAPI(
    title="Fast API PMS",
    description="PMS for managing personnel and courses.",
    version="0.0.1",
    contact={
        "name": "Balogun",
        "email": "yemibalogun2006@gmail.com",
        
    },
    license_info={
        "name": "DSA",
    }
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of the user you want to retrive")):
    return users[id]