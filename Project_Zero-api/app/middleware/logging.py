from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.orm import Session
from fastapi import Request
from ..database import database, models
from ..utils import utils



class LoggingMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, 
                       request: Request, 
                       call_next):
        
        db: Session = next(database.get_db())
        sid = request.state.sid
        url = request.url.path
        method = request.method
        ip_adress = request.client.host
        
        # Check if the user is logged in
        user_id = None
        if request.cookies.get("access_token") is not None:
            
            _, payload = await utils.verify_access_token(
                token=request.cookies.get("access_token")
            )
            user_id = payload.get("user_id")
        
        # Create a new log entry
        if user_id is not None:
            logging = models.UserActivityLogs(user_id=user_id, 
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
