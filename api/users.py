from typing import Optional, List
from fastapi import FastAPI
from fastapi import APIRouter

router = APIRouter()



@router.get("/users")
async def get_users():
    return {"message": "successful"}


@router.post("/users")
async def create_user():
    
    return "Success"


@router.get("/users/{id}")
async def get_user():
    return {"message": "successful"}