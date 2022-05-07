
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.db import Base
from app.core import hashing

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(50))
    current_booking = relationship("Booking", back_populates="customer_info")

    def __init__(self, fullName, email, password, *args, **kwargs):
       self.fullName = fullName
       self.email = email
       self.password = hashing.get_password_hash(password)
    
    def check_password(self, password):
        return hashing.verify_password(self.password, password)
