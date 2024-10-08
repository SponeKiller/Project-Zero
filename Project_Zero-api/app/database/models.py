from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.sql import text


class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone_number_prefix = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))