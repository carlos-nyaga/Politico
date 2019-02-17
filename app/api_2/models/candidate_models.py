from app.api_2.models.db_config import init_db
from app.api_2.models.connection import connection

class Candidates:
    def __init__(self):
        self.candidate_table = """ CREATE TABLE IF NOT EXISTS candidates(
        candidate_id serial  NOT NULL ,
        office_id INTEGER NOT NULL references offices(office_id),
        party_id INTEGER NOT NULL references parties(party_id),
        user_id INTEGER NOT NULL references users(user_id),
        PRIMARY KEY(office_id, user_id));"""

    def candidate_create(self, officeid, partyid, userid):
        conn = init_db(self.candidate_table)
        cur = conn.cursor()
        cur.execute(""" INSERT INTO candidates(office_id, party_id, user_id)
        VALUES('{}','{}','{}')
        RETURNING office_id, candidate_id; """.format(officeid, partyid, userid))

        candidate = cur.fetchone()
        conn.commit()
        conn.close()
        return candidate

    def candidate_exists(self, id):
        conn = connection()
        cur = conn.cursor()
        cur.execute(""" SELECT user_id, office_id FROM candidates WHERE user_id = '{}' """.format(id))
        exit = cur.fetchall()
        conn.close()
        return exit
