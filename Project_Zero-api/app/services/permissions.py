
from sqlalchemy.orm import Session
from app.database import models

def chat_exists(chat_id: int, db: Session) -> bool:
    """
    Check if a chat with the given ID exists.

    Args:
        chat_id (int): The ID of the chat.
        db (Session): The database session.

    Returns:
        bool: True if the chat exists, False otherwise.
    """
    return db.query(models.Chats).filter(models.Chats.id == chat_id).first() is not None

def is_user_chat_owner(chat_id: int, user_id: int, db: Session) -> bool:
    """
    Check if the user is the owner of the chat.
    
    Args:
        chat_id (int): The ID of the chat.
        user_id (int): The ID of the user.
        db (Session): The database session.
    """
    return db.query(models.Chats).filter(
        models.Chats.id == chat_id,
        models.Chats.user_id == user_id
    ).first() is not None