from turtle import pos
from fastapi import Depends, FastAPI
import database
import models
import routers.post,routers.user
from fastapi.middleware.cors import CORSMiddleware
models.database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routers.post.router)
app.include_router(routers.user.router)
