from fastapi import FastAPI
from app.core.config import settings
from app.api.endpoints import health, users, auth  # <-- Added auth here

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["System"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["Users"])

# Include the new Auth router
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["Authentication"])

@app.get("/", include_in_schema=False)
def root():
    return {"message": "Welcome to the Orbit API. Visit /docs for documentation."}