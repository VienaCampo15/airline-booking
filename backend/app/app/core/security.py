from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
#from typing import List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.core.config import settings
from app.user.models import User
from app.database import db
from app.auth import schema

auth2_scheme = OAuth2PasswordBearer(tokenUrl = "/login/")

def create_access_token(*, sub: str) -> str:
    return _create_token(token_type = "access_token", lifetime = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES), sub = sub)

def _create_token(token_type: str, lifetime: timedelta, sub: str) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

async def get_current_user(db: Session = Depends(db.get_db_session), token: str = Depends(auth2_scheme)) -> User:
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, 
                                          detail = "Could not validate credentials",
                                          headers = {"WWW-Authenticate":"Bearer"})
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud":False}
        )

        username = payload.get('sub')
        
        if username is None:
            raise credentials_exception
        
        token_data = schema.TokenData(username = username)
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.username == token_data.username).first()

    if user is None:
        raise credentials_exception

    return user