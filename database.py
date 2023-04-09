from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import find_dotenv , load_dotenv
import os

load_dotenv(find_dotenv())
username = os.environ.get('username')
password = os.environ.get('password')
hostname = os.environ.get('hostname')
database_name = os.environ.get('database_name')


SQL_DATABASE_URL = f'postgresql://{username}:{password}@{hostname}/{database_name}'

engine = create_engine(SQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

#dependency for talking to the database not connecting
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()