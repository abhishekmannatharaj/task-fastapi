pip install "fastapi[all]"
psycopg2

## Run fastapi
uvicorn main: app --reload

# FastAPI Instagram-Style Backend Service

A modular backend CRUD API built with **FastAPI** and **PostgreSQL**, structured according to production best practices with versioned routing and segregated schemas.

---

## Project Architecture

```text
app/
├── api/
│   └── v1/
│       └── posts/
│           ├── __init__.py
│           ├── router.py       # Posts endpoints (/api/v1/posts)
│           └── schemas.py      # Pydantic models for validation
│
├── db/
│   ├── __init__.py
│   └── database.py             # PostgreSQL connection & cursor handling
│
├── main.py                     # Minimal application entrypoint
├── requirements.txt
└── README.md

