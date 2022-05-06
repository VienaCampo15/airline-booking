from enum import Enum
from re import S
from typing import List
from sqlalchemy.orm import Session
from datetime import date

from .schema import BookingCreate, BookingUpdate
from .models import Booking

async def get_booking_by_id(id: int, db_session: Session):
    booking = db_session.query(Booking).filter(Booking.id == id).first()
    return booking

async def get_bookings_by_status_and_customer(status: str, customer_id: int, db_session: Session):
    if status == None and customer_id == None:
        bookings = db_session.query(Booking).all()

    elif status != None and customer_id == None:
        bookings = db_session.query(Booking).filter(Booking.status == status).all()

    elif status == None and customer_id != None:
        bookings = db_session.query(Booking).filter(Booking.customer_id == customer_id).all()    

    else:
        bookings = db_session.query(Booking).filter(Booking.status == status,
                                                    Booking.customer_id == customer_id).all()                                                
    return bookings

async def get_bookings_by_flight_id(flight_id: int, db_session: Session):
    bookings = db_session.query(Booking).filter(Booking.outboundFlight == flight_id).all()
    return bookings

async def create_new_booking(flight_id: int, user_id: int, booking: BookingCreate, db_session: Session) -> Booking:
    new_booking = Booking(**booking.dict(), customer_id=user_id, outboundFlight=flight_id)
    db_session.add(new_booking)
    db_session.commit()
    db_session.refresh(new_booking)

    return new_booking

async def update_booking(id: int, newBooking: BookingUpdate, db_session: Session):
    id = db_session.query(Booking).filter(Booking.id == id).update(newBooking.dict())
    db_session.commit()
    return db_session.query(Booking).filter(Booking.id == id).first()

async def delete_booking_by_id(id: int, db_session: Session):
    db_session.query(Booking).filter(Booking.id == id).delete()
    db_session.commit()
