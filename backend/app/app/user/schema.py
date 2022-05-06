from pydantic import BaseModel, constr, EmailStr

class UserBase(BaseModel):
    fullName: str
    email: EmailStr

class UserCreate(UserBase):
    password: constr(max_length=255)

class UserUpdate(UserCreate):
    pass

class UserInDBBase(UserBase):
    id: int
    password: constr(max_length=255)

    class Config:
        orm_mode = True

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
    