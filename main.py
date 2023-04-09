from fastapi import FastAPI , Response, status, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import session
import model
from database import engine, get_db
import sqlalchemy
import schemas
from typing import List
import utils 
from routers import posts
from routers import users , oauth

model.base.metadata.create_all(bind=engine)

app = FastAPI()

#loop for connecting to the database
while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database= 'fastapi', user= 'postgres', password = 'newPassword',
                                      cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection succesfull")
        break
    except Exception as error:
        print("database connection was unsuccesfull")
        print("trying to connect again...")
        time.sleep(2)



@app.get("/")
def root():
    return {"data": "good"}

@app.get("/sqlalchemy")
def test(db: session = Depends(get_db)):
    post = db.query(model.Post).all()
    print(post)
    return {"data":"good"}

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(oauth.router)