from fastapi import APIRouter
from app.core.config import settings
from app.schemas.health import HealthResponse

router = APIRouter()

@router.get(
    "/health", 
    response_model=HealthResponse,
    status_code=200,
    summary="Perform a Health Check"
)
def health_check():
    return {
        "status": "healthy",
        "version": settings.VERSION,
        "environment": "development"
    }