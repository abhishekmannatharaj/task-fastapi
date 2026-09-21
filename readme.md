# FastAPI Instagram-Style Backend Service

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791.svg?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

A modular, production-grade backend CRUD API built with **FastAPI** and **PostgreSQL**, implementing OAuth2 JWT authentication, versioned routing (`/api/v1`), and strict schema segregation.
<img width="1508" height="697" alt="img2" src="https://github.com/user-attachments/assets/d06c8145-6645-4830-b0de-f848e51a67d7" />
<img width="1872" height="872" alt="image" src="https://github.com/user-attachments/assets/31f1f097-0437-415e-9e11-4dcef487b04a" />

---

## Project Structure

```text
app/
├── api/
│   └── v1/
│       ├── auth/
│       │   ├── auth_router.py     # POST /register, POST /login
│       │   ├── security.py        # bcrypt hashing, JWT tokens, get_current_user guard
│       │   └── user_schemas.py    # UserCreate, UserResponse, Token schemas
│       └── posts/
│           ├── router.py          # Protected Post CRUD routes
│           └── schemas.py         # PostCreate, PostResponse models
├── db/
│   ├── __init__.py
│   └── database.py                # PostgreSQL engine, sessionmaker & Base
├── main.py                        # Application entrypoint & router registry
├── requirements.txt
└── README.md
```

---

## Quick Start & Local Setup

### Option 1: Local Python Environment (PowerShell)

```powershell
# Create a virtual environment
py -3 -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Install project dependencies
pip install -r requirements.txt

# Launch FastAPI development server
uvicorn app.main:app --reload
```

### Option 2: Docker Compose

```bash
# Build and run containers in detached mode
docker compose up --build -d

# Check running container status
docker compose ps

# View live container logs
docker compose logs -f

# Stop and tear down containers
docker compose down
```

---

## API Endpoints Matrix

Base URL prefix: `/api/v1`

| Method | Endpoint | Action / Operation | Auth Required? | Request Body | Response Model | Status |
| :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| `POST` | `/auth/register` | Register a new user | No | `UserCreate` (JSON) | `UserResponse` | `201` |
| `POST` | `/auth/login` | Authenticate & obtain JWT | No | `OAuth2PasswordRequestForm` | `Token` | `200` |
| `POST` | `/posts/` | Create a new post | **Yes** | `PostCreate` (JSON) | `PostResponse` | `201` |
| `GET` | `/posts/` | Retrieve all posts | No | *None* | `List[PostResponse]` | `200` |
| `GET` | `/posts/{id}` | Retrieve post by ID | No | *None* | `PostResponse` | `200` |
| `GET` | `/posts/latest` | Retrieve newest post | No | *None* | `PostResponse` | `200` |
| `PUT` | `/posts/{id}` | Replace existing post | **Yes** | `PostCreate` (JSON) | `PostResponse` | `200` |
| `DELETE`| `/posts/{id}` | Remove a post record | **Yes** | *None* | *None* | `204` |

## Next Project Reference
- **Analytics Service:** [pandas-analytics Repository](https://github.com/abhishekmannatharaj/pandas-analytics.git)

---

---

## Architecture & Design Patterns

### Request Lifecycle Workflow
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/09db7237-600f-4fd9-afc3-742230745666" />
