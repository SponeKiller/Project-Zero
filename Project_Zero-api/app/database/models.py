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
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token = Column(String, nullable=False)
    valid = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))

class CSRFTokens(Base):
    __tablename__ = "csrf_tokens"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token = Column(String, nullable=False)
    valid = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))

class UserActivityLogs(Base):
    __tablename__ = "useractivity_logs"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
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
    

class Chats(Base):
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))

class Messages(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    chat_id = Column(Integer, ForeignKey("chats.id", ondelete="CASCADE"), nullable=False)
    role = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False,
                        server_default=text("now()"))