from fastapi import FastAPI
from routes import employee, leave, balance

app = FastAPI()

app.include_router(employee.router)
app.include_router(leave.router)
app.include_router(balance.router)

@app.get("/")
def home():
    return {
        "success": True,
        "message": "API is running",
        "data": {}
    }