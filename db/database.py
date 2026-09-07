import os
import time
from pathlib import Path
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

# Find the absolute path to the root app directory where .env lives
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

db_password = os.getenv("DB_PASSWORD")

while True:
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "fastapi"),
            user=os.getenv("DB_USER", "postgres"),
            password=db_password,
            port=os.getenv("DB_PORT", "5432"),
            cursor_factory=RealDictCursor,
        )
        cursor = connection.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)