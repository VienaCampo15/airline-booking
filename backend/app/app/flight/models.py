
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey , DateTime
from sqlalchemy.orm import relationship
from database.session import Base

class Flight(Base):
    __tablename__ = 'flight'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    departureDate = Column(DateTime, default = datetime.now)
    departureAirportName = Column(String(100))
    departureAirpotCode = Column(String(100))
    departureCity = Column(String(100))
    departureLocate = Column(String(100))
    arrivalDate = Column(DateTime, default = datetime.now)
    arrivalAirportName = Column(String(100))
    arrivalAirportCode = Column(String(100))
    arrivalCity = Column(String(100))
    arrivalLocate = Column(String(100))
    ticketprice = Column(Float)
    flightNumber = Column(String(100))
    seatCapacity = Column(Integer)
    booking_info = relationship("Booking", back_populates="flight_info")