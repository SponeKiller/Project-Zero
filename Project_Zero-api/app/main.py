from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import routers as routers_v1


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(routers_v1.router)
