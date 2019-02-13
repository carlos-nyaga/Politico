import os
import psycopg2



def connection():
    conn = psycopg2.connect(
        database = os.getenv('DATABASE_NAME'),
        user = os.getenv('DATABASE_USER'),
        password = os.getenv('DATABASE_PASS'),
        host = os.getenv('DATABASE_HOST'),
        port = os.getenv('DATABASE_PORT'))
    return conn