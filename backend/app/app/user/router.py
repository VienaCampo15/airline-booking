from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date, datetime
from app.database import db
from .schema import User, UserCreate, UserUpdate
from . import services

api_router = APIRouter(tags = ["Users"])

@api_router.get("/users", response_model = List[User])
async def get_all_users(db_session: Session = Depends(db.get_db_session)):
    return await services.get_all_users(db_session)

@api_router.get("/users/{id}", response_model = User)
async def get_user_by_id(id: int, db_session: Session = Depends(db.get_db_session)):
    user = await services.get_user_by_id(id, db_session)
    if not user:
        raise HTTPException(status_code = 404, detail = "Non-existing user")
    return user

@api_router.post("/users", status_code = status.HTTP_201_CREATED, response_model = User)
async def create_new_user(user: UserCreate, db_session: Session = Depends(db.get_db_session)):
    new_user = await services.create_new_user(user, db_session = db_session)
    return new_user

@api_router.put("/users/{id}", status_code = status.HTTP_200_OK)
async def update_user(id: int, user: UserUpdate, db_session: Session = Depends(db.get_db_session)):
    new_user = await services.update_user(id, user, db_session)
    return new_user

@api_router.delete("/users/{id}", status_code = status.HTTP_200_OK, response_class = PlainTextResponse)
async def delete_user_by_id(id: int, db_session: Session = Depends(db.get_db_session)):
    await services.delete_user_by_id(id, db_session)
    return "The user have been deleted."