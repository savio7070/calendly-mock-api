import json
from datetime import datetime, timedelta

def get_available_slots(date: str, appointment_type: str):
    with open("data/doctor_schedule.json", "r") as f:
        schedule = json.load(f)

    working_hours = schedule.get("working_hours", [])
    booked_slots = [b["start_time"] for b in schedule.get("booked", []) if b["date"] == date]

    duration_map = {
        "consultation": 30,
        "followup": 15,
        "physical": 45,
        "specialist": 60
    }

    duration = duration_map.get(appointment_type.lower(), 30)
    slots = []

    for slot in working_hours:
        if slot["start_time"] in booked_slots:
            available = False
        else:
            available = True
        slots.append({
            "start_time": slot["start_time"],
            "end_time": slot["end_time"],
            "available": available
        })
    return slots
