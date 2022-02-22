from os import access
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import schemas, utils, models, oauth, database 
router = APIRouter(tags=['Authentication'])

@router.post("/login")
async def Login(user_credentials: OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"Invalid credentials")
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    access_token  =oauth.create_access_token(data={"user_id":user.id,"user_mail":user.email})

    return {"access_token": access_token,"token_type": "bearer"}