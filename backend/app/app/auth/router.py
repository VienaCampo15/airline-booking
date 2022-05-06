from typing import Any
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.database import db
from app.user.services import authenticate

api_router = APIRouter(tags=["Auth"])

@api_router.post("/login/")
def login(db_session: Session= Depends(db.get_db_session), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = authenticate(email=form_data.username, password=form_data.password, db_session=db_session)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    return {
        "access_token": create_access_token(sub=user.email),
        "token_type": "Bearer",
    }