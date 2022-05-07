from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import date

from app.core import hashing

from .schema import UserCreate, UserUpdate
from .models import User

async def create_new_user(user: UserCreate, db_session: Session) -> User:
    new_user = User(**user.dict())
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)

    return new_user

async def get_all_users(db_session: Session) -> List[User]:
    users = db_session.query(User).all()
    return users

async def get_user_by_id(id: int, db_session: Session) -> User:
    user = db_session.query(User).filter(User.id == id).first()
    return user

async def update_user(id: int, newUser: UserUpdate, db_session: Session) -> User:
    id = db_session.query(User).filter(User.id == id).update(newUser.dict())
    db_session.commit()
    return db_session.query(User).filter(User.id == id).first()

async def delete_user_by_id(id: int, db_session: Session):
    db_session.query(User).filter(User.id == id).delete()
    db_session.commit()

def authenticate(*, email: str, password: str, db_session = Session) -> Optional[User]:
    user = db_session.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not hashing.verify_password(password, user.password):
        return None
    
    return user