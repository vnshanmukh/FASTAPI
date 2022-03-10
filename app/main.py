from ensurepip import version
from fastapi import Depends, FastAPI
import routers.post,routers.user,routers.auth,routers.vote
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
#models.Base.metadata.create_all(bind=database.engine)
version = 'v1.0.0'
description = """API for social media app"""
app = FastAPI(
    title= "MEDIA API",
    version =version,
    description  = description
)
favicon_path = 'favicon.ico'
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/favicon.ico',include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.get('/')
async def home():
    return {
        "title": "FASTAPI",
        "version" : version,
        "description" : description,
        "documentation" : "http://143.244.143.151/docs"
    }

app.include_router(routers.post.router)
app.include_router(routers.user.router)
app.include_router(routers.auth.router)
app.include_router(routers.vote.router)