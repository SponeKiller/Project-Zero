from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..utils.config import settings

Base = declarative_base()

DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(DATABASE_URL)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
