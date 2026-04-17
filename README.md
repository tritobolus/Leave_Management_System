# Leave Management System API (FastAPI)

## Overview

This project is a **Leave Management System API** built using **FastAPI (Python)**.
It provides RESTful endpoints to manage employees, leave requests, and leave balances.

The system is designed as a lightweight backend for HR operations with JSON-based data storage.

---

##  Features

### Employee Management

* Create new employees
* Retrieve all employees
* Retrieve employee by ID

### Leave Management

* Apply for leave
* Automatic calculation of total leave days
* Leave status tracking (Pending, Approved, Rejected)
* Retrieve leaves by employee ID

### Leave Balance Management

* Track leave balances (Annual, Sick, Casual)
* Auto-create balance when employee is created
* Fetch leave balance by employee and year

---

## Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Database:** JSON file (`database.json`)
* **Documentation:** Swagger UI (auto-generated)

---

## 📁 Project Structure

```
leave-management-api/
│
├── main.py
├── database.json
├── requirements.txt
│
├── routes/
│   ├── employee.py
│   ├── leave.py
│   └── balance.py
│
├── models/
│   ├── employee.py
│   └── leave.py
│
└── utils/
    └── db.py
```

---

## Setup Instructions

### Clone the repository

```
git clone <your-repo-link>
cd leave-management-api
```

### Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the server

```
uvicorn main:app --reload
```

---

## API Documentation

Once the server is running:

* 🔗 Swagger UI:
  `http://127.0.0.1:8000/docs`

* 🔗 OpenAPI JSON:
  `http://127.0.0.1:8000/openapi.json`

---

## API Endpoints

### Employees

* `GET /api/employees` → Get all employees
* `GET /api/employees/{id}` → Get employee by ID
* `POST /api/employees` → Create employee

---

### Leaves

* `POST /api/leaves` → Apply for leave
* `GET /api/leaves/employee/{id}` → Get leaves by employee

---

### Leave Balances

* `GET /api/leavebalances/employee/{id}/year/{year}` → Get leave balance

---

## Sample Data

The `database.json` file is pre-populated with:

* 5 Employees
* Leave records
* Leave balance records for multiple years

---

## Response Format

All API responses follow a consistent structure:

```json
{
  "success": true,
  "message": "Action message",
  "data": {}
}
```

---

## Key Functionalities

* Automatic leave day calculation
* Leave type validation using Enum
* Date validation using Pydantic
* Thread-safe JSON file operations
* Auto-generated API documentation

---

## Deployment

The API is deployed and accessible at:

👉 **Live API URL:**
`<your-deployment-link>`

---

## 🔗 Repository

👉 **GitHub Repository:**
`https://github.com/tritobolus/Leave_Management_System`

---

##  Conclusion

This project demonstrates:

 Backend API development using FastAPI
 Modular architecture
 Data validation and processing
 RESTful API design

---

 Thank you for reviewing this project!
