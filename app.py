from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi import Path

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

@app.get("/employee/{emp_id}")
def get_employee(

    emp_id:int = Path(
        gt=0,
        lt=100,
        description="Employee ID must be between 1 and 99"
    )

):
    return{
        "Employee ID":emp_id
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