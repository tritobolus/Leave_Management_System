from fastapi import APIRouter
from utils.db import read_db

router = APIRouter(prefix="/api/leavebalances", tags=["Balances"])

@router.get("/employee/{id}/year/{year}")
def get_balance(id: int, year: int):
    db = read_db()

    balances = [
        b for b in db["balances"]
        if b["employeeId"] == id and b["year"] == year
    ]

    return {
        "success": True,
        "message": "Balance fetched",
        "data": balances
    }