from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Task Model
class Task(BaseModel):
    title: str
    description: str

# Task storage with IDs
tasks = []
task_id_counter = 1

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}

# Create a new task
@app.post("/tasks")
def create_task(task: Task):
    global task_id_counter
    
    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description
    }
    
    tasks.append(new_task)
    task_id_counter += 1
    
    return {"message": "Task added successfully", "task": new_task}

# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# Update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            return {"message": "Task updated successfully", "task": task}
    
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    
    raise HTTPException(status_code=404, detail="Task not found")
