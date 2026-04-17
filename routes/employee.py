from fastapi import APIRouter
from models.employee import Employee
from utils.db import read_db, write_db
from datetime import datetime

router = APIRouter(prefix="/api/employees", tags=["Employees"])

# GET all employees
@router.get("/")
def get_employees():
    db = read_db()
    return {
        "success": True,
        "message": "All employees fetched",
        "data": db["employees"]
    }

# CREATE employee
@router.post("/")
def create_employee(emp: Employee):
    db = read_db()

    emp_id = len(db["employees"]) + 1

    new_emp = {
    "employeeId": emp_id,
    "firstName": emp.firstName,
    "lastName": emp.lastName,
    "email": emp.email,
    "department": emp.department,
    "joinDate": emp.joinDate.isoformat()   
}

    # Added employee
    db["employees"].append(new_emp)

    # create default leave balance when emp created
    current_year = datetime.now().year

    new_balance = {
        "employeeId": emp_id,
        "year": current_year,
        "Annual": 20,
        "Sick": 10,
        "Casual": 7
    }

    db["balances"].append(new_balance)

    write_db(db)

    return {
        "success": True,
        "message": "Employee created",
        "data": new_emp
    }