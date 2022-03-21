from typing import Optional, List
from fastapi import FastAPI
from api import users, courses, sections

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
        "name": "MIT",
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

