import openai
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from typing import List, Dict

from app.utils.config import settings



class OpenAI:
    def __init__(self, api_key: str, model: str = None) -> None:
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model
        
    def available_models(self):
        return self.client.models()    
        
    def query(self, query: List[Dict[str, str]]) -> ChatCompletionMessage:
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=query
        )
        return response.choices[0].message
                  

def get_chat() -> OpenAI:
    """
    Get chat instance
    """
    return OpenAI(
        api_key=settings.openai_api_key, 
        model=settings.openai_model
    )


