from app.api_2.models.db_config import init_db
from werkzeug.security import generate_password_hash
import jwt, datetime, time,os
from app.api_2.models.connection import connection
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

    def hash(self, password):
       hashed_pass = generate_password_hash(password)
       return hashed_pass
    def to_dict(self, user):
        data = {
        'id': user[0],
        'first_name': user[1],
        'email': user[2],
        'isadmin': user[3]
            }
        return data

    def auth_token_encode(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                os.getenv('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, os.getenv('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def user_create(self, fname, lname, oname,email,phoneNo, passport, password, isadmin ):
        conn = init_db(self.user_table)
        cur = conn.cursor()
        cur.execute(""" INSERT INTO users (first_name, last_name, other_name, email, phone_number, passport_url, password, isadmin)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')  RETURNING user_id, first_name, email, isadmin; """.format(fname, lname, oname, email, phoneNo,passport, Users.hash(password), isadmin))

        user = cur.fetchone()
        conn.commit()
        conn.close()
        return Users().to_dict(user)

    def login(self, email, password):
        conn = connection()
        cur = conn.cursor()
        id = cur.execute(""" SELECT user_id FROM users WHERE users.email = '{}' AND users.password = '{}'; """.format(email, Users().hash(password)))
        conn.commit()
        conn.close()
        return Users().auth_token_encode(id)

    

