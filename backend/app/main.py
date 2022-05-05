from fastapi import FastAPI
from app.core import config
from app.catalogue import router as catalogue_router

'''from app.database import models
from app.catalogue import router as flight_router
from app.booking import router as booking_router
from app.user import router as user_router'''

app = FastAPI(title = "Airline-Booking", version = "0.0.1")

app.include_router(catalogue_router.api_router)