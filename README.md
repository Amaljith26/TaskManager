# 🧠 Unix-Inspired Task Manager API (Django)

This is a Django-based REST API project that mimics Unix-like task management functionality, offering endpoints similar to `ls` (list tasks) and `fork` (create tasks). It includes authentication and a minimal web interface for testing.


🔐 User login (preconfigured for a single user: `amal`)
- 📄 List tasks (GET)
- ➕ Create tasks (POST)
- 📦 SQLite database
- 🧪 Simple UI + API-friendly design


## 👤 Default User Credentials

| Username | Password |
|----------|----------|
| `amal`   | `amal`   |

## 🛠️ Setup Instructions


1. Installation
git clone https://github.com/your-username/task-manager.git
cd task-manager

2. Set Up the Virtual Environment
python -m venv env
env\Scripts\activate  # On Windows

3. Install Requirements
pip install -r requirements.txt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

▶️ Run the Development Server
python manage.py runserver
Visit: http://127.0.0.1:8000/

 Using the API
🔑 Login (Session Auth)
Use the browser login at /accounts/login/
POST /accounts/login/
{
  "username": "amal",
  "password": "amal"
}

GET: List Tasks (ls Equivalent)
GET /tasks/

POST /tasks/create/
{
  "title": "New Task",
  "description": "This is a task created via API."
}

taskmanager/
├── tasks/               
├── templates/           
├── db.sqlite3         
├── manage.py
└── README.md

 To-Do / Future Features
✅ Per-user task isolation
⏳ Task status (done, pending, in-progress)
⏳ Due dates and priorities


API Documentation
Endpoints

1. Create Task
URL: /create_task/
Method: POST
name: The name of the task.
description: A detailed description of the task.
status: The current status of the task (In Progress, Completed, Pending).

3. List Tasks
URL: /task_manager/
Method: GET
Returns a list of tasks, categorized by their status (In Progress, Completed, Pending).

4. Delete Task
URL: /delete_task/<task_id>/
Method: POST
Deletes a task by its ID.



