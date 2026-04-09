from pydantic import BaseModel, Field

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