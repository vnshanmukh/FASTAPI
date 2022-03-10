from fastapi import Depends, FastAPI
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'app'))
import routers.post,routers.user,routers.auth,routers.vote
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
#models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
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

app.include_router(routers.post.router)
app.include_router(routers.user.router)
app.include_router(routers.auth.router)
app.include_router(routers.vote.router)