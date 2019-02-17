import psycopg2
from app.api_2.models.connection import connection

def tables():
    users_table = """ CREATE TABLE IF NOT EXISTS users(
                user_id serial PRIMARY KEY NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                other_name VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL UNIQUE,
                phone_number VARCHAR(50) NOT NULL UNIQUE,
                passport_url VARCHAR(50) NOT NULL,
                password VARCHAR(500) NOT NULL,
                ispolitician BOOLEAN,
                isadmin BOOLEAN);"""

    offices_table = """ CREATE TABLE IF NOT EXISTS offices(
                office_id serial PRIMARY KEY NOT NULL,
                office_name character varying(50) NOT NULL,
                office_type character varying(50) NOT NULL);"""

    parties_table = """ CREATE TABLE IF NOT EXISTS parties(
                party_id serial PRIMARY KEY NOT NULL,
                party_name character varying(50) NOT NULL,
                hqAddress character varying(50) NOT NULL,
                logoUrl character varying(50) NOT NULL);"""

    candidates_table = """ CREATE TABLE IF NOT EXISTS candidates(
                candidate_id serial  NOT NULL ,
                office_id INTEGER NOT NULL references offices(office_id),
                party_id INTEGER NOT NULL references parties(party_id),
                user_id INTEGER NOT NULL references users(user_id),
                PRIMARY KEY(office_id, user_id));"""

    tables = [users_table, offices_table, parties_table, candidates_table]
    conn = connection()
    cur = conn.cursor()
    for table in tables:
        cur.execute(table)
    conn.commit()
    conn.close()
        

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
    candidates = """ DROP TABLE IF EXISTS candidates CASCADE; """

    queries = [users, parties, offices, candidates]

    for query in queries:
        cur.execute(query)
    conn.commit()
    conn.close()
    tables()
