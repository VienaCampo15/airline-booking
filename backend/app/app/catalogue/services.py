from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from datetime import date

from . import schema
from . import models
from app.booking import models as bookingModels

async def get_all_flights(db_session: Session) -> List[models.Flight]:
    flights = db_session.query(models.Flight).all()
    return flights

async def get_flights_by_airportsCode_and_date(departureAirportCode: str, arrivalAirportCode: str, departureDate: date, db_session: Session):
    dac = db_session.query(models.Flight).filter(models.flight.departureAirportCode == departureAirportCode).all()
    if not dac:
        raise HTTPException(status_code = 404, detail = "Departure airport code not found")
    
    aac = db_session.query(models.Flight).filter(models.flight.arrivalAirportCode == departureAirportCode).all()
    if not dac:
        raise HTTPException(status_code = 404, detail = "Arrival airport code not found")
    
    flights = db_session.query(models.Flight).filter(models.Flight.departureAirportCode == departureAirportCode,
                                                    models.Flight.arrivalAirportCode == arrivalAirportCode,
                                                    func.date(models.Flight.departureDate) == departureDate).all()
    return flights

async def get_flights_by_airport_and_departureDate(departureAirportCode: str, departureDate: date, db_session: Session):
    dac = db_session.query(models.Flight).filter(models.flight.departureAirportCode == departureAirportCode).all()
    if not dac:
        raise HTTPException(status_code = 404, detail = "Departure airport code not found")
    
    if departureDate:
        flights = db_session.query(models.Flight).filter(models.Flight.departureAirportCode == departureAirportCode,
                                                    func.date(models.Flight.departureDate) == departureDate).all()
    else: flights = dac
    return flights

async def create_new_flight(flight: schema.FlightCreate, db_session: Session) -> models.Flight:
    flight = models.Flight(**flight.dict())
    db_session.add(flight)
    db_session.commit()
    db_session.refresh(flight)

async def update_flight(flight_id: int, newFlight: schema.FlightUpdate, db_session: Session):
    flight = db_session.query(models.Flight).filter(models.Flight.id == id).update(newFlight.dict())
    db_session.commit()
    return flight

async def delete_flight_by_id(flight_id: int, db_session: Session):
    db_session.query(models.Flight).filter(models.Flight.id == flight_id).delete()
    db_session.commit()
