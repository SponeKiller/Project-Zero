
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from uuid import uuid4



class SIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        sid = request.cookies.get("sid") or str(uuid4())
        
        request.state.sid = sid
            
        response = await call_next(request)
        
        response.set_cookie(key="sid", value=sid, httponly=True)
        
        return response