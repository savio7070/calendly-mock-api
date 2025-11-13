from fastapi import FastAPI
from backend.api.calendly_integration import router as calendly_router

app = FastAPI(title="Calendly Mock API")

app.include_router(calendly_router, prefix="/api/calendly", tags=["Calendly"])

@app.get("/")
def root():
    return {"message": "Calendly Mock API is running!"}
