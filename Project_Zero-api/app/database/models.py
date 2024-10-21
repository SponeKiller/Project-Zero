from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
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
    
class RefreshTokens(Base):
    __tablename__ = "refresh_tokens"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String, nullable=False)
    valid = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))

class CSRFToken(Base):
    __tablename__ = "csrf_tokens"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String, nullable=False)
    valid = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))