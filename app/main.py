from turtle import pos
from fastapi import Depends, FastAPI
import database
import models
import routers.post,routers.user

models.database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.include_router(routers.post.router)
app.include_router(routers.user.router)
