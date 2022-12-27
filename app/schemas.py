from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    """
    defines structure of a request/response. ensures that when a user creates a 
    post, the request will only go through if it has these values
    """
    course: str
    duration: Optional[str]
    effort: Optional[str]
    link: Optional[str]
    year: int
    comments: Optional[str]
 
class PostCreate(PostBase):
    """
    inherits from PostBase. defines the structure of a request
    """ 
    pass

class PostResponse(PostBase): 
    """
    inherits from PostBase. defines the structure of a response. controls what 
    is output to the user
    """
    id: int
    created_at: datetime
    owner_id: int
    class Config: #outputs the response even if it is not a dict
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime
    class Config: #outputs the response even if it is not a dict
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token = str
    token_type = str

class TokenData(BaseModel):
    id: Optional[str] = None