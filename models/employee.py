from pydantic import BaseModel
from datetime import date

class Employee(BaseModel):
    firstName: str
    lastName: str
    email: str
    department: str
    joinDate: date  