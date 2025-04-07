import phonenumbers

from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from ..schemas import user as schema
from app.database import database
from app.database import models
from app.utils.config import settings
from app.utils import utils
from .token import login





pwd_context = CryptContext(schemes=[settings.pwd_context_scheme],
                           deprecated="auto")


router = APIRouter(prefix="/users",
                   tags=["authentications"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def register(response: Response,
                   user: schema.UserRegister,
                   db: Session = Depends(database.get_db)):
    
    
    retrieved_user = db.query(models.Users).filter(
        models.Users.email == user.email
    ).first()
    
    if retrieved_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User already exists")
    
    user_phone_number = phonenumbers.parse(user.phone_number)
    
    new_user = models.Users(email=user.email,
                            username=user.username,
                            password=pwd_context.hash(user.password),
                            phone_number_prefix=user_phone_number.country_code,
                            phone_number=user_phone_number.national_number)
    
    db.add(new_user)
    db.commit()
    
    db.refresh(new_user)
    