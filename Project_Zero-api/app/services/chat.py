from sqlalchemy.orm import Session
from typing import List, Dict
from fastapi import HTTPException, status

from .openai import OpenAI
from app.database import database
from app.database import models
from .permissions import chat_exists, is_user_chat_owner

def send_and_log_message(
    chat: OpenAI,
    messages: List[Dict[str, str]],
    chat_id: int,
    db: Session
) -> str:
    """
    Send a message to the chat model and log the response.
    """
    
    # Send the message to the chat model
    response = chat.query(query=messages)
    messages.append({"role": response.role, "content": response.content})
    
    # Create database session
    db = next(database.get_db())

    # Writing messages to db
    for message in messages:
        role = message.get("role")
        content = message.get("content")
        
        new_message = models.Messages(
            chat_id=chat_id,
            role=role,
            content=content
        )
        
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        
        message["id"] = new_message.id
        
    return messages

def verify_chat_access(chat_id: int, user_id: int, db: Session) -> None:
    
    """
    Verify existance of chat and user ownership.
    
    Args:
        chat_id (int): ID of the chat.
        user_id (int): ID of the user.
        db (Session): Database session.
    Raises:
        HTTPException: If the chat does not exist or the user is not the owner.
    """
    
    if not chat_exists(chat_id=chat_id, db=db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Chat not found"
        )

    if not is_user_chat_owner(chat_id=chat_id, user_id=user_id, db=db):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="You are not the owner of this chat"
        )
 