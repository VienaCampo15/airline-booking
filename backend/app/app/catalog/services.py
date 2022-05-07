from typing import List
from sqlalchemy.orm import Session
from datetime import date

from . import schema
from . import models

async def get_all_flights(db_session: Session) -> List[models.Flight]:
    flights = db_session.query(models.Flight).all()
    return flights

async def get_flights_by_airportsCode_and_date(departureAirportCode: str, arrivalAirportCode: str, departureDate: date, db_session: Session):
    flights = db_session.query(models.Flight).filter(models.Flight.departureAirportCode == departureAirportCode,
                                                    models.Flight.arrivalAirportCode == arrivalAirportCode,
                                                    models.Flight.departureDate == departureDate).all()
    return flights

async def get_flights_by_airport_and_departureDate(departureAirportCode: str, departureDate: date, db_session: Session):
    if departureDate != None:
           flights = db_session.query(models.Flight).filter(models.Flight.departureAirportCode == departureAirportCode,
                                                    models.Flight.departureDate == departureDate).all()
    else:
           flights = db_session.query(models.Flight).filter(models.Flight.departureAirportCode == departureAirportCode).all()                                                    
    return flights

async def create_new_flight(flight: schema.FlightCreate, db_session: Session) -> models.Flight:
    new_flight = models.Flight(**flight.dict())
    db_session.add(new_flight)
    db_session.commit()
    db_session.refresh(new_flight)

    return new_flight

async def update_flight(id: int, newFlight: schema.FlightUpdate, db_session: Session):
    id = db_session.query(models.Flight).filter(models.Flight.id == id).update(newFlight.dict())
    db_session.commit()
    return db_session.query(models.Flight).filter(models.Flight.id == id).first()

async def delete_flight_by_id(id: int, db_session: Session):
    db_session.query(models.Flight).filter(models.Flight.id == id).delete()
    db_session.commit()
