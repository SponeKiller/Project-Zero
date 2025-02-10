from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
import pytz
from typing import Tuple
import secrets
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from .config import settings
from ..database import database, models
class TokenData(BaseModel):
    access_token: str
    token_type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict) -> str:
    
    to_encode = data.copy()
    
    expire = create_UTC_exp_time(int(settings.access_token_expire_minutes))
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, 
                             settings.secret_key, 
                             algorithm=settings.algorithm)
    
    return encoded_jwt

def verify_access_token(
    token: str = Depends(oauth2_scheme),
    credentials_exception: HTTPException = None
) -> TokenData:
    
    try:
        payload = jwt.decode(token,
                             settings.secret_key,
                             algorithms=settings.algorithm)
        
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = TokenData(id=id)
        
    except JWTError:
        raise credentials_exception
    
    return token_data, payload


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(database.get_db)) -> models.Users:
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Your access token is invalid, expired or missing",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token = verify_access_token(token, credentials_exception)
    
    user = db.query(models.Users).filter(models.Users.id == token.id).first()
    
    return user



def create_refresh_token() -> Tuple:
    
    expire = create_UTC_exp_time(int(settings.refresh_token_expire_minutes))
    
    token = secrets.token_hex(int(settings.refresh_token_length))
    
    return token, expire

def verify_refresh_token(token: str,
                         user_id: int,
                         db: Session = Depends(database.get_db)) -> bool:
        
    is_valid = (
        db.query(models.RefreshTokens.valid)
        .order_by(desc(models.RefreshTokens.id))
        .filter(
            models.RefreshTokens.user_id == user_id, 
            models.RefreshTokens.token == token
        )
        .first()
    )
    
    return is_valid

def create_csrf_token() -> str:
    
    token = secrets.token_hex(int(settings.csrf_token_length))   
    
    return token


def create_UTC_exp_time(minutes: int) -> datetime:
    
    expire = (
        datetime.now(timezone.utc) 
        + timedelta(minutes=minutes)
    )
    
    return expire

