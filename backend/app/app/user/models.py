
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Email
from sqlalchemy.orm import relationship
from database.session import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String(300))
    email = Column(String(250), Email)
    password = Column(String(50))
    current_booking = relationship("Booking", back_populates="flight_info")