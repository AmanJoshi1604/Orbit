from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Orbit API"
    VERSION: str = "1.0.0"
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI: str = "postgresql://orbit_user:orbit_password@localhost:5432/orbit_db"

    # Security Configuration
    SECRET_KEY: str = "generate-a-super-secret-key-here" 
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        case_sensitive = True

settings = Settings()