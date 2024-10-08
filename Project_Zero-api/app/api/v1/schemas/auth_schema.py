from pydantic import BaseModel


class UserToken(BaseModel):

    access_token: str
    token_type: str
  
  