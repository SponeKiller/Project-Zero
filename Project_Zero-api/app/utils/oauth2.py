from jose import JWTError, jwt
from datetime import datetime, timedelta
import pytz
from ..database import database, models
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from .config import settings

class TokenData(BaseModel):
    access_token: str
    token_type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict):
    
    to_encode = data.copy()
    
    expire = (
        datetime.now(pytz.utc) 
        + timedelta(minutes=settings.access_token_expire_minutes)
    
    )
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, 
                             settings.secret_key, 
                             algorithm=settings.algorithm)
    
    return encoded_jwt

def verify_access_token(token: str = Depends(oauth2_scheme),
                         credentials_exception: HTTPException = None):
    
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
    
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(database.get_db)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Your access token is invalid, expired or missing",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token = verify_access_token(token, credentials_exception)
    
    user = db.query(models.Users).filter(models.Users.id == token.id).first()
    
    return user
