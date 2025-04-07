from fastapi import APIRouter

from app.utils import utils
from .endpoints import token
from .endpoints import user
from .endpoints import chat



router = APIRouter(prefix="/api/v1")

# Non - Secure Routes
router.include_router(token.router)
router.include_router(user.router)

# Secure Routes
utils.include_secure_router(router, chat.router)

