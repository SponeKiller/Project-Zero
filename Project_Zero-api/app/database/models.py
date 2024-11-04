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

class CSRFTokens(Base):
    __tablename__ = "csrf_tokens"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String, nullable=False)
    valid = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))

class UserActivityLog(Base):
    __tablename__ = "page_tracing"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    sesion_id = Column(String, nullable=False)
    ip_adress = Column(String, nullable=False)
    endpoint = Column(String, nullable=False)
    method = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))
    
class SessionLogs(Base):
    __tablename__ = "session_logs"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    session_id = Column(String, nullable=False)
    ip_adress = Column(String, nullable=False)
    endpoint = Column(String, nullable=False)
    method = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))