from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from enum import Enum
from dotenv import load_dotenv
import os
import openai

# Load all the environment variables
load_dotenv()

API_KEY = os.getenv("OPEN_API_SECRET_KEY")



class OperatorChoice(str, Enum):
    addition = "ADDITION"
    subtraction = "SUBTRACTION"
    multiplication = "MULTIPLICATION"
    
class RequestSchema(BaseModel):
    operation_type: OperatorChoice
    x: int
    y: int
    
class ResponseSchema(BaseModel):
    slackUsername : Optional[str] = "Nengi_Tammy"
    result: int
    operation_type: OperatorChoice 

app = FastAPI()

@app.get("/")
def root():
    return{"message": "WELCOME TO THE HNG BACKEND TASK 2 PROJECT"}

def calculate_x_y(x, y, operator):
    if operator == OperatorChoice.addition:
        return x + y
    if operator == OperatorChoice.subtraction:
        return abs(x - y)
    if operator == OperatorChoice.multiplication:
        return x * y

    

@app.post("/calculate", status_code= status.HTTP_200_OK, response_model=ResponseSchema)
def calculate(data: RequestSchema):
    x = data.x
    y = data.y
    operator = data.operation_type
    result = calculate_x_y(x ,y, operator)
    return {"slackUsername" : "Nengi_Tammy",
            "result": result,
            "operation_type" : operator}


