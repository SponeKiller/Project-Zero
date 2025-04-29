from pydantic import BaseModel
from typing import List, Literal

class MessageIn(BaseModel):
    role: Literal["system", "user"]
    content: str

class MessageOut(BaseModel):
    id: int
    role: Literal["system", "user", "assistant"]
    content: str
    
class ChatMessageIn(BaseModel):
    messages: List[MessageIn]
    
class ChatMessageOut(BaseModel):
    messages: List[MessageOut]

class ChatOutput(BaseModel):
    id: int
    
class ChatListOut(BaseModel):
    chats: List[int]

