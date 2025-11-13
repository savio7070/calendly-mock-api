# Calendly Mock API

## Overview
A simple FastAPI backend simulating Calendly-like scheduling for medical appointments.

### Endpoints
- **GET /api/calendly/availability?date=YYYY-MM-DD&appointment_type=consultation**
- **POST /api/calendly/book**

### Example Booking Request
```json
{
  "appointment_type": "consultation",
  "date": "2025-11-12",
  "start_time": "09:00",
  "patient": {
    "name": "Sakshi Sharma",
    "email": "sakshi@example.com",
    "phone": "+91-7247454851"
  },
  "reason": "General checkup"
}
```

### Run Locally
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Visit: http://127.0.0.1:8000/docs
