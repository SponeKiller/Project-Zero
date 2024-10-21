from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import phonenumbers
from ..schemas import register_schema
from ....database import database
from ....utils.config import settings
from ....utils import oauth2
from ....database import models




pwd_context = CryptContext(schemes=[settings.pwd_context_scheme],
                           deprecated="auto")


router = APIRouter(tags=["authentications"])

router.post("/register")
async def register(response: Response,
                   user: register_schema.UserRegister,
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
    
    access_token = oauth2.create_access_token({"user_id": new_user.id})
    
    response.set_cookie(key="access_token",
                        value=f"Bearer {access_token}",
                        httponly=True)
    