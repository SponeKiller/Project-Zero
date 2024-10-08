from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserRegister(BaseModel):
    email: EmailStr
    username: str
    password: str
    phone_number: PhoneNumber

   

