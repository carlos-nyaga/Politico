from app.api_2.models.db_config import init_db
from app.api_2.models.connection import connection

class Offices:
    def __init__(self):
        self.office_table = """ CREATE TABLE IF NOT EXISTS offices(
        office_id serial PRIMARY KEY NOT NULL,
        office_name character varying(50) NOT NULL,
        office_type character varying(50) NOT NULL);"""


    def office_create(self, officename, type):
        conn = init_db(self.office_table)
        cur = conn.cursor()
        cur.execute(""" INSERT INTO offices (office_name, office_type)
        VALUES('{}','{}')
        RETURNING office_id, office_name, office_type; """.format(officename, type))

        office = cur.fetchone()
        conn.commit()
        conn.close()
        return office

    def office_get(self, id = None):
        conn = connection()
        cur = conn.cursor()
        if id:
            cur.execute(""" SELECT office_id, office_name, office_type FROM offices WHERE office_id = '{}'; """.format(id))
            office = cur.fetchall()
            conn.close()
            data = {
                "office_id": office[0][0],
                "office_name" : office[0][1],
                "office_type": office[0][2]
                }
            return data

        else:
            cur.execute(""" SELECT office_id, office_name, office_type FROM offices ; """)
            offices = cur.fetchall()
            conn.close()
            data = []
            for office in offices:
                office = {
                    "office_id": office[0],
                    "office_name": office[1],
                    "office_type": office[2]
                }

                data.append(office)
            return data

    def office_exists(self, id):
        conn = connection()
        cur = conn.cursor()
        cur.execute(""" SELECT office_id from offices WHERE office_id = '{}'; """.format(id))
        exist = cur.fetchall()
        conn.close()
        return exist 
        
    def name_exists(self, name):
        conn = connection()
        cur = conn.cursor()
        cur.execute(""" SELECT office_name from offices WHERE office_name = '{}' ;""".format(name))
        exist = cur.fetchall()
        conn.close()
        return exist