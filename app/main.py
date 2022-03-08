from fastapi import Depends, FastAPI
import models , routers.post,routers.user,routers.auth,routers.vote , database
from fastapi.middleware.cors import CORSMiddleware
models.Base.metadata.create_all(bind=database.engine)
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
app.include_router(routers.auth.router)
app.include_router(routers.vote.router)