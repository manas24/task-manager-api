from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Task Model (structure of task)
class Task(BaseModel):
    title: str
    description: str

# Temporary storage (in-memory database)
tasks: List[Task] = []

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}

# Create a new task
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task added successfully", "task": task}

# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks
