from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import get_password_hash
from app.api.deps import get_current_user

router = APIRouter()

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user"
)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user_in.password)
    
    db_user = User(
        email=user_in.email,
        username=user_in.username,
        hashed_password=hashed_password
    )
    
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
        
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email or username already exists."
        )

@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current user"
)
def read_current_user(current_user: User = Depends(get_current_user)):
    """
    Fetches the profile of the currently logged-in user.
    Requires a valid JWT token.
    """
    return current_user