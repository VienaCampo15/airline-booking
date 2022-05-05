from pydantic import BaseModel, constr
from datetime import datetime

class FlightBase(BaseModel):
    departureDate = datetime
    departureAirportName = str
    departureAirpotCode = constr(max_length = 50)
    departureCity = str
    departureLocate = str
    arrivalDate = datetime
    arrivalAirportName = str
    arrivalAirportCode = constr(max_length = 50)
    arrivalCity = str
    arrivalLocate = str
    ticketprice = float
    flightNumber = int
    seatCapacity = int

class FlightCreate(FlightBase):
    pass

class FlightUpdate(FlightBase):
    pass

class FlightInDBBase(FlightBase):
    id: int

    class Config:
        orm_mode = True

class Flight(FlightInDBBase):
    pass

class FightInDB(FlightInDBBase):
    pass