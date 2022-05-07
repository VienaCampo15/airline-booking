from app.user import schema as user_schema
from app.core import security
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date, datetime
from app.database import db
from . import services
from .schema import Booking, BookingCreate, BookingUpdate

api_router = APIRouter(tags = ["Booking"])

@api_router.get("/booking/{id}", response_model = Booking)
async def get_booking_by_id(id: int, db_session: Session = Depends(db.get_db_session)):
    return await services.get_booking_by_id(id, db_session)

@api_router.get("/booking", response_model = List[Booking])
async def get_bookings_by_status_and_customer(status: Optional[str] = None, customer_id: Optional[int] = None, db_session: Session = Depends(db.get_db_session)):
    bookings = await services.get_bookings_by_status_and_customer(status, customer_id, db_session)
    if not bookings:
        raise HTTPException(status_code = 404, detail = "Non-existing bookings")
    return bookings

@api_router.get("/booking/flight/{id}", response_model = List[Booking])
async def get_bookings_by_flight_id(id: int, db_session: Session = Depends(db.get_db_session)):
    bookings = await services.get_bookings_by_flight_id(id, db_session)
    if not bookings:
        raise HTTPException(status_code = 404, detail = "Non-existing bookings")
    return bookings

@api_router.post("/booking/flight/{flight_id}/user/{user_id}", status_code = status.HTTP_201_CREATED, response_model = Booking)
async def create_new_booking(flight_id: int, user_id: int, booking: BookingCreate, db_session: Session = Depends(db.get_db_session),
                             current_user: user_schema.User = Depends(security.get_current_user)):
    new_booking = await services.create_new_booking(flight_id, user_id, booking, db_session = db_session)
    return new_booking

@api_router.delete("/booking/{id}", status_code = status.HTTP_200_OK, response_class = PlainTextResponse)
async def delete_booking_by_id(id: int, db_session: Session = Depends(db.get_db_session),
                                current_user: user_schema.User = Depends(security.get_current_user)):
    await services.delete_booking_by_id(id, db_session)
    return "The booking have been deleted."