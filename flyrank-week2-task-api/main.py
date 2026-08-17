from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# ---------- Database ----------
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a CRUD API", "done": False},
    {"id": 3, "title": "Submit assignment", "done": False},
]
next_id = 4
# ------------------------------

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})
    return task

# ---------- Create ----------
class TaskCreate(BaseModel):
    title: str

@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    if not task_data.title or not task_data.title.strip():
        raise HTTPException(status_code=400, detail={"error": "Title is required and cannot be empty"})
    global next_id
    new_task = {"id": next_id, "title": task_data.title.strip(), "done": False}
    tasks.append(new_task)
    next_id += 1
    return new_task

# ---------- Stage 4: Update & Delete ----------
class TaskUpdate(BaseModel):
    title: str | None = None  # Optional, because user might only update 'done'
    done: bool | None = None

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})

    # If they sent a title, validate it
    if task_data.title is not None:
        if not task_data.title or not task_data.title.strip():
            raise HTTPException(status_code=400, detail={"error": "Title cannot be empty"})
        task["title"] = task_data.title.strip()
    
    # If they sent a done status, update it
    if task_data.done is not None:
        task["done"] = task_data.done
    
    return task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # Find the index of the task
    task_index = next((i for i, t in enumerate(tasks) if t["id"] == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})
    
    tasks.pop(task_index)
    # Returning nothing automatically sends the 204 No Content body
    return