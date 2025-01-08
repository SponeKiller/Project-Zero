from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import routers as routers_v1
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.sid_middleware import SIDMiddleware
from app.utils.config import settings

app = FastAPI()

#Middleware

##CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=True,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)

##HTTP
#app.add_middleware(SIDMiddleware)
#app.add_middleware(LoggingMiddleware)



#Routing

##API v1
app.include_router(routers_v1.router)

