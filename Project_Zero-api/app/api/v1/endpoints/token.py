from fastapi import APIRouter, Response, Depends, HTTPException, status, Cookie, Security
from fastapi.security import OAuth2PasswordRequestForm, HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from ..schemas import token as schema
from app.database import database
from app.database import models
from app.utils.config import settings
from app.utils import utils


bearer_scheme = HTTPBearer()

pwd_context = CryptContext(schemes=[settings.pwd_context_scheme],
                           deprecated="auto")


router = APIRouter(prefix="/token",
                   tags=["authentications"])

@router.post("", response_model=schema.Token)
async def login(response: Response,
                user_credentials: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(database.get_db)) -> schema.Token:
    
    user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    
    if not pwd_context.verify(user_credentials.password,
                              user.password):
        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    
    
    access_token = utils.create_access_token({"user_id": user.id})
    refresh_token, refresh_token_expires = utils.create_refresh_token()
    csrf_token = utils.create_csrf_token()
    
    response.set_cookie(key="refresh_token",
                        value=f"{refresh_token}",
                        httponly=True,
                        secure=True,
                        samesite="strict",
                        expires=refresh_token_expires)
    
    response.set_cookie(key="csrf_token",
                        value=f"{csrf_token}",
                        secure=True,
                        samesite="strict")
    
    return {"access_token": access_token,   
            "token_type": "bearer"}
    
@router.get("/me", response_model=schema.TokenData)
async def me(
    credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)
):
    
    token_data = utils.verify_access_token(credentials.credentials)
    
    return token_data


@router.post("/refresh", response_model=schema.Token)  
async def refresh(response: Response,
                  user: schema.SessionUser,
                  refresh_token: str = Cookie(None),
                  db: Session = Depends(database.get_db)) -> schema.Token:
    
    user = db.query(models.Users).filter(
        models.Users.id == user.user_id
    ).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    
    if not utils.verify_refresh_token(refresh_token):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    
    
    access_token = utils.create_access_token({"user_id": user.id})
    
    return {"access_token": access_token,   
            "token_type": "bearer"}
    

@router.delete("")
async def logout(response: Response):
    
    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")
    response.delete_cookie(key="csrf_token")