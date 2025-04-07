from datetime import datetime, timedelta, timezone
from typing import Tuple
import secrets

from fastapi import HTTPException, APIRouter, status, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy import desc
from jose import JWTError, jwt

from .config import settings
from ..database import database, models


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict) -> str:
    
    to_encode = data.copy()
    
    expire = create_UTC_exp_time(int(settings.access_token_expire_minutes))
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, 
                             settings.secret_key, 
                             algorithm=settings.algorithm)
    
    return encoded_jwt

def verify_access_token(token: str = Depends(oauth2_scheme)) -> dict:
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Your access token is invalid, expired or missing",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token,
                             settings.secret_key,
                             algorithms=settings.algorithm)
        

        if payload.get("user_id") is None:
            raise credentials_exception

        
    except JWTError:
        
        raise credentials_exception
    
    return payload


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(database.get_db)) -> models.Users:
    
    
    token = verify_access_token(token)
    
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

async def verify_and_store_user(
    request: Request,
    payload=Depends(verify_access_token),
):
    """
    Verify the access token and store the user in the request state.
    
    Args:
        request (Request): The HTTP request object.
        payload (dict): The decoded JWT payload.
    """
    
    request.state.user = payload


def include_secure_router(main_router: APIRouter, subrouter: APIRouter) -> None:
    """
    Include a secure router with token verification.
    
    Args:
        main_router (APIRouter): The main router to include the subrouter in.
        subrouter (APIRouter): The subrouter to be included.

    """
    main_router.include_router(
        subrouter,
        dependencies=[Depends(verify_and_store_user)]
    )

