from fastapi import APIRouter
from models.leave import Leave
from utils.db import read_db, write_db
from datetime import datetime

router = APIRouter(prefix="/api/leaves", tags=["Leaves"])

def calculate_days(start, end):
    return (end - start).days + 1

# Apply leave
@router.post("/")
def apply_leave(leave: Leave):
    db = read_db()

    leave_id = len(db["leaves"]) + 1
    days = calculate_days(leave.startDate, leave.endDate)

    new_leave = {
    "leaveId": leave_id,
    "employeeId": leave.employeeId,
    "startDate": leave.startDate.isoformat(),
    "endDate": leave.endDate.isoformat(),
    "leaveType": leave.leaveType.value,
    "reason": leave.reason,
    "totalDays": days,
    "status": "Pending"
}

    db["leaves"].append(new_leave)
    write_db(db)

    return {
        "success": True,
        "message": "Leave applied",
        "data": new_leave
    }

# GET leaves by employee id
@router.get("/employee/{id}")
def get_leaves(id: int):
    db = read_db()

    leaves = [l for l in db["leaves"] if l["employeeId"] == id]

    return {
        "success": True,
        "message": "Leaves fetched",
        "data": leaves
    }