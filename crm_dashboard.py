from sqlalchemy import create_engine

DB_USER = "your_db_user"
DB_PASS = "your_db_password"
DB_HOST = "your_project.supabase.co"
DB_PORT = "5432"
DB_NAME = "postgres"

DB_URL = f"postgresql://postgres:mzYH28tlOTskENy7@db.uhakcwvfbtrijvlttjno.supabase.co:5432/postgres"
engine = create_engine(DB_URL)
