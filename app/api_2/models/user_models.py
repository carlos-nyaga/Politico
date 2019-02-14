from app.api_2.models.db_config import init_db
from werkzeug.security import generate_password_hash
class Users:
    def __init__(self):
        self.user_table =  """ CREATE TABLE IF NOT EXISTS users(
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

    
    def to_dict(self, user):
        data = {
        'id': user[0],
        'first_name': user[1],
        'email': user[2],
        'isadmin': user[3]
            }
        return data

    def user_create(self, fname, lname, oname,email,phoneNo, passport, password, isadmin ):
        conn = init_db(self.user_table)
        cur = conn.cursor()
        cur.execute(""" INSERT INTO users (first_name, last_name, other_name, email, phone_number, passport_url, password, isadmin)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')  RETURNING user_id, first_name, email, isadmin; """.format(fname, lname, oname, email, phoneNo,passport, generate_password_hash(password), isadmin))

        user = cur.fetchone()
        conn.commit()
        conn.close()
        return Users().to_dict(user)

    

