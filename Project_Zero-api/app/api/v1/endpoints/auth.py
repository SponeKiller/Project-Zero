from fastapi import APIRouter, Response, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..schemas import auth_schema
from ....database import database
from ....utils.config import settings
from ....utils import oauth2
from ....database import models


pwd_context = CryptContext(schemes=[settings.pwd_context_scheme],
                           deprecated="auto")


router = APIRouter(tags=["authentications"])

@router.post("/token")
async def login(response: Response,
                user_credentials: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(database.get_db)):
    
    user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    
    if not pwd_context.verify(user_credentials.password,
                              user.password):
        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    
    
    access_token = oauth2.create_access_token({"user_id": user.id})
    
    response.set_cookie(key="access_token",
                        value=f"Bearer {access_token}",
                        httponly=True)


