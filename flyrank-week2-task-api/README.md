# Task CRUD API

A simple RESTful API built with **FastAPI** to manage a to-do list. Supports full CRUD operations with in-memory storage. Built as a Week 2 assignment for the FlyRank Backend AI Engineering track.

## Setup & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Angel-ai1612/flyrank.git
   cd flyrank/flyrank-week2-task-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   Open your browser at [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

## Endpoints

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| GET | `/` | API information | 200 |
| GET | `/health` | Health check | 200 |
| GET | `/tasks` | List all tasks | 200 |
| GET | `/tasks/{id}` | Get a single task | 200, 404 |
| POST | `/tasks` | Create a new task | 201, 400 |
| PUT | `/tasks/{id}` | Update a task | 200, 400, 404 |
| DELETE | `/tasks/{id}` | Delete a task | 204, 404 |

## Example `curl` Output

```bash
$ curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'
HTTP/1.1 201 Created
...
{"id":4,"title":"Buy milk","done":false}
```

## Swagger UI

![Swagger UI](swagger.png)
**4. Push to GitHub:**
```bash
git add requirements.txt .gitignore README.md
git commit -m "Stage 6: publish and docs"

# Create repo on GitHub first, then link and push
git remote add origin https://github.com/your-username/flyrank-week2-task-api.git
git branch -M main
git push -u origin main