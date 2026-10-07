from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Properties to receive on user creation
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

# Properties to return to the client
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool
    is_creator: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy models