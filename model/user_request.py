from datetime import date

from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    email: str = Field(max_length=255, pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    age: int = Field(gt=0, lt=150)
    address: str = Field(min_length=1, max_length=300)
    joining_date: date
