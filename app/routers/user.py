import models,schemas
from fastapi import Depends, FastAPI,Response,HTTPException,status, APIRouter
from sqlalchemy.orm import Session
import database

router = APIRouter(
    prefix= "/users",
    tags=['users']
)
@router.post("/", response_model=schemas.UserOut)
async def create_user(user:schemas.UserCreate,db: Session = Depends(database.get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=schemas.UserOut)
async def get_user(id:int, db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
    return user
