import psycopg2
from app.api_2.models.db_config import init_db

def test_connection():
    query = """ CREATE TABLE IF NOT EXISTS offices(
        office_id serial PRIMARY KEY NOT NULL,
        office_name character varying(50) NOT NULL,
        office_type character varying(50) NOT NULL);"""


    try:
        init_db(query)
    
    except Exception as e:
        return e