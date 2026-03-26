# Fundoo Notes App

A backend REST API built using **FastAPI** for managing users and notes.
This project demonstrates CRUD operations, database integration, logging, and modular architecture.

## Tech Stack

* **FastAPI** – Backend framework
* **SQLAlchemy** – ORM for database operations
* **Microsoft SQL Server (MSSQL)** – Database
* **Pydantic** – Data validation
* **Uvicorn** – ASGI server
* **Python Logging** – Application logging


## Project Structure

```
Fundoo-app/
│
├── main.py
├── database/
│   └── db.py
│
├── models/
│   ├── user_models.py
│   └── note_model.py
│
├── schemas/
│   ├── schema_user.py
│   └── note_schema.py
│
├── routes/
│   ├── routes_users.py
│   └── routes_notes.py
│
├── services/
│   ├── user_service.py
│   └── note_service.py
│
├── utils/
│   └── logger.py
│
├── logs/
│   └── app.log
│
└── requirements.txt
```


## Setup Instructions
---

### 1. Create Virtual Environment

```
python -m venv myenv
```

Activate (Windows):

```
myenv\Scripts\activate
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```


### 3. Configure Database (MSSQL)

Update connection string in `database/db_connect.py`:


Ensure:

* SQL Server is running
* Database `FundooDB` is created

---

### 4. Run Application

```
uvicorn main:app --reload
```

---

## API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## Features

### User Management

* Create User
* Get Users
* Update User
* Delete User

### Notes Management

* Create Note
* Get All Notes
* Get Notes by User
* Update Note
* Delete Note

---


## Logging

* Logs are stored in:

```
logs/app.log
```

* Logs include:

  * API activity
  * Errors
  * Database operations

---

## Future Enhancements

*  Password Hashing (bcrypt)
*  Pagination
*  Search functionality
*  created_at & updated_at fields

---

## Learning Outcomes

* REST API development
* SQLAlchemy ORM usage
* MSSQL integration
* Logging implementation

---

