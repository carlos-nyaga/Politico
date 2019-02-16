import psycopg2
from app.api_2.models.connection import connection



def init_db(query):
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

    users = """ DROP TABLE IF EXISTS users CASCADE; """
    parties = """ DROP TABLE IF EXISTS parties CASCADE; """
    offices = """ DROP TABLE IF EXISTS offices CASCADE; """

    queries = [users, parties, offices]

    for query in queries:
        cur.execute(query)
    conn.commit()
    conn.close()
