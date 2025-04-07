from fastapi import APIRouter, Request, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.openai import OpenAI, get_chat
from ..schemas import chat as schema
from app.database import database
from app.database import models
from app.services.chat import send_and_log_message, verify_chat_access




router = APIRouter(prefix="/chats",
                   tags=["messages"])


@router.get("/{chat_id}/messages", response_model=schema.ChatMessageOut)
async def retrieve_chat(
    request: Request,
    chat_id: int,
    db: Session = Depends(database.get_db)
) -> schema.ChatMessageOut:
    """
    Retrieve all messages in chat.
    """
    
    verify_chat_access(
        chat_id=chat_id,
        user_id=request.state.user['user_id'],
        db=db
    )
    
    # Retrieve and return all messages in the chat
    messages = db.query(
        models.Messages.role,
        models.Messages.content,
        models.Messages.id
    ).filter(
        models.Messages.chat_id == chat_id
    ).all()

    return {"messages": messages}

@router.post("", response_model=schema.ChatOutput)
async def create_chat(
    request: Request,
    db: Session = Depends(database.get_db)
) -> schema.ChatOutput:
    """
    Create a chat
    """
    
    # Create Chat in database
    new_chat = models.Chats(
        user_id = request.state.user['user_id']
    )
    
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    
    return {"chat_id": new_chat.id}
    
    

@router.post("/{chat_id}/messages", response_model=schema.ChatMessageOut)
async def send_message(
    request: Request,
    chat_id: int,
    messages: schema.ChatMessageIn,
    db: Session = Depends(database.get_db),
    chat: OpenAI = Depends(get_chat)
) -> schema.ChatMessageOut:
    """
    Send a message to the chat model and return the response.
    """
    
    verify_chat_access(
        chat_id=chat_id,
        user_id=request.state.user['user_id'],
        db=db
    )

    # Generate a response from AI model
    messages = send_and_log_message(
        chat=chat,
        messages=messages.model_dump()["messages"],
        chat_id=chat_id,
        db=db
    )
    
    return {"messages": messages}


@router.delete("/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_chat(
    request: Request,
    chat_id: int,
    db: Session = Depends(database.get_db)
) -> None:
    """
    Delete whole chat
    """
    
    verify_chat_access(
        chat_id=chat_id,
        user_id=request.state.user['user_id'],
        db=db
    )
    
    # Delete chat 
    db.query(models.Chats).filter(models.Chats.id == chat_id).delete()
    
    db.commit()

@router.delete("/{chat_id}/messages", status_code=status.HTTP_204_NO_CONTENT)
async def delete_messages(
    request: Request,
    chat_id: int,
    messages: schema.ChatMessageDel,
    db: Session = Depends(database.get_db)
) -> None:
    """
    Delete messages from chat
    """
    
    verify_chat_access(
        chat_id=chat_id,
        user_id=request.state.user['user_id'],
        db=db
    )
    
    # Check if all messages exist in the database
    input_ids = {m["id"] for m in messages.model_dump()["messages"]}

    existing_ids = {
        row[0] for row in db.query(models.Messages.id).filter(
            models.Messages.chat_id == chat_id
        ).all()
    }

    missing_ids = input_ids - existing_ids
    
    if missing_ids:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Message(s) with id(s) {missing_ids} not found in chat."
        )
    
    # Delete messages from the database
    db.query(models.Messages) \
        .filter(models.Messages.chat_id == chat_id) \
        .filter(models.Messages.id.in_([m["id"] for m in messages.model_dump()["messages"]])) \
        .delete()
    
    db.commit()