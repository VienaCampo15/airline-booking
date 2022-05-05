from fastapi import APIRouter, Depends, status, Response, HTTPException
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from app.database import db
from . import schema
from . import services

api_router = APIRouter(tags = ["Catalogo"])

@api_router.get("/catalogo/all", response_model = List[schema.Flight])
async def get_all_flights(db_session: Session = Depends(db.get_db_session)):
    return await services.get_all_flights(db_session)

@api_router.get("/catalogo/", response_model = List[schema.Flight])
async def get_flights_by_airportsCode_and_date(departureAirportCode: str, arrivalAirportCode: str, departureDate: date, db_session: Session = Depends(db.get_db_session)):
    flights = await services.get_flights_by_airportsCode_and_date(departureAirportCode, arrivalAirportCode, departureDate, db_session)
    if not flights:
        raise HTTPException(status_code = 404, detail = "Non-existing flights")
    return flights

@api_router.get("/catalogo/{airportCode}", response_model = List[schema.Flight])
async def get_flights_by_airport_and_departureDate(airportCode: str, departureDate: Optional[date] = None, db_session: Session = Depends(db.get_db_session)):
    flights = await services.get_flights_by_airport_and_departureDate(airportCode, departureDate, db_session)
    if not flights:
        raise HTTPException(status_code = 404, detail = "Non-existing flights")
    return flights

@api_router.post("/catalogo", status_code = status.HTTP_201_CREATED, response_model = schema.Flight)
async def create_new_flight(flight: schema.FlightCreate, db_session: Session = Depends(db.get_db_session)):
    new_flight = await services.create_new_flight(flight, db_session = db_session)
    return new_flight

@api_router.put("/catalogo/{id}", status_code = status.HTTP_201_CREATED)
async def update_flight(flight_id: int, flight: schema.FlightUpdate, db_session: Session = Depends(db.get_db_session)):
    new_flight = await services.update_flight(id, flight, db_session)

@api_router.delete("catalogo/{id}", status_code = status.HTTP_200_OK, response_class = PlainTextResponse)
async def delete_flight_by_id(id: int, db_session: Session = Depends(db.get_db_session)):
    await services.delete_flight(id, db_session)
    return "The flight have been deleted."