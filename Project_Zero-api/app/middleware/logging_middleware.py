from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.orm import Session
from fastapi import Request
from ..database import database, models
from ..utils import utils



class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        db: Session = await database.get_db()
        
        sid = getattr(request.state, "sid")
        url = request.url.path
        method = request.method
        ip_adress = request.client.host
        
        _, payload = await utils.verify_access_token(
            token=request.cookies.get("access_token")
        )
        user_id = payload.get("user_id")
        
        if user_id:
            logging = models.UserActivityLog(user_id=user_id, 
                                             session_id=sid,
                                             ip_adress=ip_adress,
                                             endpoint=url,
                                             method=method)
        else:
            logging = models.SessionLogs(session_id=sid,
                                         ip_adress=ip_adress,
                                         endpoint=url,
                                         method=method)
        db.add(logging)
        db.commit()
        
        response = await call_next(request)
        
        return response
