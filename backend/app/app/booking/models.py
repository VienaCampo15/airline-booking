
from datetime import datetime
from unicodedata import name
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.session import Base
from flight.models import Flight
from user.models import User

class BookingStatus(Base):
    __tablename__ = "bookingStatus"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    status_info = relationship("Booking", back_populates = "status")
    

class Booking(Base):
    __tablename__ = "booking"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    status_id = Column(Integer, ForeignKey('bookingStatus.id', ondelete="CASCADE"))   
    costumer = Column(String(300), ForeignKey(User.id, ondelete="CASCADE"))
    createdAt = Column(DateTime, default=datetime.now)
    outboundFlight = Column(Integer,ForeignKey(Flight.id, ondelete="CASCADE"))
    flight_info = relationship("Flight", back_populates="booking_info")
    status=relationship("BookingStatus", back_populates="status_info")
    user_info = relationship("User", back_populates="current_booking")
    