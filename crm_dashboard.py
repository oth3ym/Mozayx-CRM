import os
from sqlalchemy import create_engine

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

DB_URL = f"postgresql://postgres:mzYH28tlOTskENy7@db.uhakcwvfbtrijvlttjno.supabase.co:5432/postgres"
engine = create_engine(DB_URL)
