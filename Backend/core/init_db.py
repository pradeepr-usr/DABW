import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_ADMIN_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_ADMIN_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("DATABASE_NAME")
DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")

def create_database_and_user():
    conn = psycopg2.connect(
        dbname="postgres",
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}'")
    db_exists = cur.fetchone()
    if not db_exists:
        cur.execute(f'CREATE DATABASE {DB_NAME};')
        print(f"Database {DB_NAME} created.")
    else:
        print(f"Database {DB_NAME} already exists.")

    cur.execute(f"SELECT 1 FROM pg_roles WHERE rolname='{DB_USER}'")
    user_exists = cur.fetchone()
    if not user_exists:
        cur.execute(f"CREATE USER {DB_USER} WITH PASSWORD '{DB_PASSWORD}';")
        cur.execute(f"GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER};")
        print(f"User {DB_USER} created with privileges on {DB_NAME}.")
    else:
        print(f"User {DB_USER} already exists.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    create_database_and_user()
