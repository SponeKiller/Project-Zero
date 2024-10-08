from fastapi import APIRouter, Depends
from .endpoints import auth
from .endpoints import register
from .endpoints import users
from ...utils import oauth2



router = APIRouter(prefix="/api/v1")


router.include_router(auth.router)
router.include_router(register.router)
router.include_router(users.router, dependencies=[Depends(oauth2.get_current_user)])
