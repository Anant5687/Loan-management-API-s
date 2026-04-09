from pydantic import BaseModel, Field

from typing import Optional
from datetime import datetime

from enum import Enum

class Occupation(str, Enum):
    SALARIED = "salaried"
    BUSINESSMAN = "businessman"
    SELF_EMPLOYED = "self_employed"
    PROFESSIONAL = "professional"   # doctor, CA, lawyer
    GOVERNMENT = "government"
    FREELANCER = "freelancer"


class User(BaseModel):
    name: str
    age: int = Field(gt=15, lt=120)
    occupation: Occupation
    yearly_income: int = Field(gt=100000, lt=100000000)
    phone : str

class Status(str, Enum):
    APPROVED= "APPROVED"
    REJECTED= "REJECTED"
    PENDING = "PENDING"    

class Loans(BaseModel):
    required_amt: int
    user_id: str
    status: Status = Field(default=Status.PENDING)


class UpdateLoan(BaseModel):
    status: Status
    comment: Optional[str] = None