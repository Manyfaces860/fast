from sqlalchemy.sql.expression import null, text
from sqlalchemy import Column, Integer, Boolean, String, TIMESTAMP
from database import base 


class Post(base):
    __tablename__ = "posts"
    
    id = Column(Integer , primary_key= True , nullable= False)
    title = Column(String, nullable= False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    
class User(base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key= True , nullable= False)
    email = Column(String , unique=True , nullable = False)
    password = Column(String , nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    
    