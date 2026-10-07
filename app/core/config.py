from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Orbit API"
    VERSION: str = "1.0.0"
    
    # Database Configuration (Add these so SQLAlchemy can connect!)
    SQLALCHEMY_DATABASE_URI: str = "postgresql://orbit_user:orbit_password@localhost:5432/orbit_db"

    class Config:
        case_sensitive = True

# THIS IS THE CRITICAL LINE THAT IS LIKELY MISSING
settings = Settings()