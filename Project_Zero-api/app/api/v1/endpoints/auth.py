from fastapi import APIRouter, Response, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..schemas import auth_schema
from ....database import database
from ....utils.crud import user_crud 


router = APIRouter(tags=["authentications"])

@router.post("/login", response_model=auth_schema.UserToken)
async def login(response: Response,
                user_credential: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(database.get_db)):
    
    user = user_crud.get_by_email(db, user_credential.username)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    
    if not user_crud.verify_password(db,
                                     user_credential.password,
                                     user.password):
        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    
    
    access_token = user_crud.create_access_token({"user_id": user.id})
    
    response.set_cookie(key="access_token",
                        value=f"Bearer {access_token}",
                        httponly=True)


