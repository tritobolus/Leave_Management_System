from pydantic import BaseModel
from datetime import date
from enum import Enum

# allowed leave types
class LeaveType(str, Enum):
    Annual = "Annual"
    Sick = "Sick"
    Casual = "Casual"

class Leave(BaseModel):
    employeeId: int
    startDate: date
    endDate: date
    leaveType: LeaveType 
    reason: str