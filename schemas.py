from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import Optional
class PostBase(BaseModel):
    
    title : str
    content : str
    published : bool = True
    
class PostCreate(PostBase):
    pass
    
    
class POST(PostBase):
    id : int
    title : str
    content : str
    published : bool 
    

    class config:
        orm_mode = True
        
class UserBase(BaseModel):
    
    email : EmailStr
    password : str
    
class UserCreate(UserBase):
    pass

class UserOut(BaseModel):
    
    id : int
    email : EmailStr
    
    class config:
        orm_mode = True
        
class login_cred(BaseModel):
    email: EmailStr
    password : str
    
class Token(BaseModel):
    access_token: str
    token_type : str
    
class Tokendata(BaseModel):
    id : Optional[str] = None