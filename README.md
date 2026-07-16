# Task Management API

A secure Task Management REST API built using Django REST Framework with JWT Authentication.

## Features

- User Registration
- JWT Authentication (Login)
- Create Task
- View Tasks
- Update Task
- Delete Task
- Task Filtering
- Unit Testing

## Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite
- JWT Authentication
- Postman
- Git & GitHub

## API Endpoints

### Authentication

POST /api/register/

POST /api/token/

### Tasks

GET /api/tasks/

POST /api/tasks/

GET /api/tasks/{id}/

PUT /api/tasks/{id}/

DELETE /api/tasks/{id}/

### Filter Tasks

GET /api/tasks/?completed=true

GET /api/tasks/?completed=false

## Testing

Run the tests using:

```bash
python manage.py test
```

## Project Structure

```
TaskManagementAPI/
│
├── config/
├── tasks/
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

## Author

**Bhavitha Bai Gaddale**
