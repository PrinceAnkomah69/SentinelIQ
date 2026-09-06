from fastapi import FastAPI

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