from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Literal

class ContactUsMessageSchema(BaseModel):
    email: EmailStr
    message: str

    class Config:
        from_attributes = True

class CreateContactUsMessageSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    subject_inquiry: Literal["GI", "BI", "CI"] = "GI"  # Default set to General Inquiry
    message: str

    class Config:
        from_attributes = True


class ClientRegistrationSchema(BaseModel):
    message: str
    email: EmailStr

    class Config:
        from_attributes = True

class CreateClientRegistrationSchema(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True


class ErrorResponseSchema(BaseModel):
    message: str
