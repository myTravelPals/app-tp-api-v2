from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Literal

class ContactUsMessageSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    subject_inquiry: Literal["GI", "BI", "CI"]  # Enum for inquiry choices
    message: str
    status: Literal["PE", "PR", "RE", "CO"]  # Enum for status choices
    date_submitted: date

    class Config:
        orm_mode = True

class CreateContactUsMessageSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    subject_inquiry: Literal["GI", "BI", "CI"] = "GI"  # Default set to General Inquiry
    message: str

    class Config:
        orm_mode = True


class ClientRegistrationSchema(BaseModel):
    id: int
    email: EmailStr
    date_registered: date

    class Config:
        orm_mode = True

class CreateClientRegistrationSchema(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True