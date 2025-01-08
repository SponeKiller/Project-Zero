import phonenumbers

from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from ..schemas import users_schema
from app.database import database
from app.database import models
from app.utils.config import settings
from app.utils import utils





pwd_context = CryptContext(schemes=[settings.pwd_context_scheme],
                           deprecated="auto")


router = APIRouter(
    prefix="/users",
    tags=["authentications"])


router.post("/", status_code=status.HTTP_201_CREATED)
async def register(response: Response,
                   user: users_schema.UserRegister,
                   db: Session = Depends(database.get_db)):
    
    user_phone_number = phonenumbers.parse(user.phone_number)
    
    new_user = models.Users(email=user.email,
                            username=user.username,
                            password=pwd_context.hash(user.password),
                            phone_number_prefix=user_phone_number.country_code,
                            phone_number=user_phone_number.national_number
                            )
    
    db.add(new_user)
    db.commit()
    
    db.refresh(new_user)
    
    access_token = utils.create_access_token({"user_id": new_user.id})
    
    response.set_cookie(key="access_token",
                        value=f"Bearer {access_token}",
                        httponly=True)
    