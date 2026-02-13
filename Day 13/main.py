from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, StrictBool, ConfigDict
from typing import Optional, List

app = FastAPI()

# In-memory database
tasks_db = []
current_id = 1


# =========================
# Models
# =========================

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: StrictBool = False   # STRICT validation


class TaskResponse(TaskCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# Routes
# =========================

# GET all tasks
@app.get("/api/tasks", response_model=List[TaskResponse])
def get_tasks():
    return tasks_db


# GET single task
@app.get("/api/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# CREATE task
@app.post("/api/tasks", status_code=201, response_model=TaskResponse)
def create_task(task: TaskCreate):
    global current_id

    new_task = task.model_dump()   # Pydantic v2 correct method
    new_task["id"] = current_id

    tasks_db.append(new_task)
    current_id += 1

    return new_task


# UPDATE task
@app.put("/api/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskCreate):
    for task in tasks_db:
        if task["id"] == task_id:
            task.update(updated_task.model_dump())
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# DELETE task
@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            tasks_db.remove(task)
            return {"message": "Task deleted successfully"}  # return 200

    raise HTTPException(status_code=404, detail="Task not found")
