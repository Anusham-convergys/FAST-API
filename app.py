from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi import Path
from fastapi import Query

app = FastAPI()
class Employee(BaseModel):
    id:int
    name: str
    deptartment: str
    salary: float
    passwword:str

class EmployeeResponse(BaseModel):
    id:int
    name:str
    department:str
    
@app.get("/")
def home():
    return{
        "message": "Employee Management API"
    }    
@app.post("/employee")
def add_employee(employee:Employee):
    return{
        "message":"Employee Added",
        "data" : employee
    }    

@app.get("/search")
def search(
    name: str = Query(
        min_length=3,
        max_length=20,
        description="Enter employee name"
    )
):
    return {
        "name": name
    }
    
@app.put("/employee/{emp_id}")
def update_employee(emp_id:int,employee:Employee):
    return{
        "message" : "Employee updated",
        "Emploee ID": emp_id,
        "data" : employee
    }    
@app.delete("/employee/{emp_id}")
def delete_employee(emp_id:int):
    return{
        "message": "Employee Deleted",
        "Employee ID": emp_id
    }    