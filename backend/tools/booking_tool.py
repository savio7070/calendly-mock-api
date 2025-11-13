import json, random, string

def book_slot(booking):
    with open("data/doctor_schedule.json", "r") as f:
        schedule = json.load(f)

    # Check if slot already booked
    for b in schedule.get("booked", []):
        if b["date"] == booking.date and b["start_time"] == booking.start_time:
            return None

    booking_id = f"APPT-{booking.date.replace('-', '')}-{random.randint(100,999)}"
    confirmation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    new_booking = {
        "booking_id": booking_id,
        "status": "confirmed",
        "confirmation_code": confirmation_code,
        "details": booking.dict()
    }

    # Add to booked list
    schedule["booked"].append({"date": booking.date, "start_time": booking.start_time})
    with open("data/doctor_schedule.json", "w") as f:
        json.dump(schedule, f, indent=4)

    with open("data/bookings.json", "r+") as f:
        data = json.load(f)
        data.append(new_booking)
        f.seek(0)
        json.dump(data, f, indent=4)

    return new_booking
