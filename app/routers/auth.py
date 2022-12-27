from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import session
import database, schemas, models, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), 
db: session = Depends(database.get_db)):
    """
    searches for the user in the database, and returns a bearer token if the 
    user provides valid credentials
    """
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
        detail=f"Invalid credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
        detail=f"Invalid credentials")
    access_token = oauth2.create_access_token(data = {"user_id" : user.id})
    return {"access token" : access_token, "token_type" : "bearer"}


