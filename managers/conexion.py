import os
import psycopg
from typing import Generator
from dotenv import load_dotenv

load_dotenv()
passwordDB = os.getenv("SUPABASE_PASSWORD")

url = f"postgresql://postgres:{passwordDB}@db.jybgnwyohacwuqagmswh.supabase.co:5432/postgres"

def getCursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()
