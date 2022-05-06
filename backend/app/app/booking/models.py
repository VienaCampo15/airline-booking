from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db import Base
from app.catalogue.models import Flight
from app.user.models import User


class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(50))   
    customer_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"))
    createdAt = Column(DateTime, default=datetime.now)
    outboundFlight = Column(Integer, ForeignKey(Flight.id, ondelete="CASCADE"))

    flight_info = relationship("Flight", back_populates="booking_info")
    customer_info = relationship("User", back_populates="current_booking")
    