from fastapi import FastAPI

from backend.risk_engine import calculate_dti, interpret_dti, calculate_risk_score
from backend.schemas import BorrowerApplication


app = FastAPI(
    title="SentinelIQ API",
    description="Backend API for the SentinelIQ financial risk intelligence platform.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "SentinelIQ API is running",
        "status": "healthy",
        "version": "0.1.0",
    }


@app.post("/risk-assessment")
def risk_assessment(application: BorrowerApplication):
    dti = calculate_dti(application)
    dti_result = interpret_dti(dti)
    risk_result = calculate_risk_score(application)

    return {
        "borrower_assessment": {
            "dti": dti_result,
            "risk": risk_result,
        }
    }