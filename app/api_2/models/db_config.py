import psycopg2
import psycopg2.extras
import os
from app.api_2.models.connection import connection



def init_db(query):
    destroy_db()
    conn = connection()
    print("init_db Opened database succesfully")
    cur = conn.cursor()
    queries = []
    queries.append(query)

    for query in queries:
        cur.execute(query)
    conn.commit()
    return conn

def destroy_db():
    conn = connection()
    print("Destroy_db Opened database succesfully")
    cur = conn.cursor()

    users = """ DROP TABLE IF EXISTS users; """
    parties = """ DROP TABLE IF EXISTS parties; """
    offices = """ DROP TABLE IF EXISTS offices; """

    queries = [users, parties, offices]

    for query in queries:
        cur.execute(query)
    conn.commit()
