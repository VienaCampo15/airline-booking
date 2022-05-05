
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship
from app.database.db import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String(300))
    email = Column(EmailType)
    password = Column(String(50))
    current_booking = relationship("Booking", back_populates="costumer_info")