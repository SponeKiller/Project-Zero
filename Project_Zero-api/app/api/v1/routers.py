from fastapi import APIRouter
from .endpoints import token
from .endpoints import users



router = APIRouter(prefix="/api/v1")


router.include_router(token.router)
router.include_router(users.router)
