from fastapi import FastAPI
from pydantic import BaseModel

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

@app.get("/employee/{emp_id}", 
         response_model=EmployeeResponse)
def get_employee(emp_id:int):
    return{
        "id":emp_id,
        "name":"Anusha",
        "department":"AI",
        "salary":90000
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