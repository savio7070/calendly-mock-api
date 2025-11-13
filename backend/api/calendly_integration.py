import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import APIRouter, HTTPException
from backend.tools.availability_tool import get_available_slots
from backend.tools.booking_tool import book_slot
from backend.models.schemas import BookingRequest

router = APIRouter()

@router.get("/availability")
def get_availability(date: str, appointment_type: str):
    slots = get_available_slots(date, appointment_type)
    return {
        "date": date,
        "appointment_type": appointment_type,
        "available_slots": slots
    }

@router.post("/book")
def book_appointment(booking: BookingRequest):
    result = book_slot(booking)
    if not result:
        raise HTTPException(status_code=400, detail="Slot not available or already booked.")
    return result


@router.get("/ping")
def ping():
    return {"message": "Calendly API working fine!"}