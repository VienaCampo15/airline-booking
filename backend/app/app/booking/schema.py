from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class BookingStatus(str, Enum):
    UNCONFIRMED = "UNCONFIRMED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"


class BookingBase(BaseModel):
    status: BookingStatus
    createdAt: datetime
    

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BookingBase):
    pass

class BookingInDBBase(BookingBase):
    customer_id: int
    outboundFlight = int
    id: int

    class Config:
        orm_mode = True

class Booking(BookingInDBBase):
    pass

class BookingInDB(BookingInDBBase):
    pass