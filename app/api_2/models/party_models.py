from app.api_2.models.db_config import init_db
from app.api_2.models.connection import connection

class Parties:
    def __init__(self):
        self.party_table = """ CREATE TABLE IF NOT EXISTS parties(
        party_id serial PRIMARY KEY NOT NULL,
        party_name character varying(50) NOT NULL,
        hqAddress character varying(50) NOT NULL,
        logoUrl character varying(50) NOT NULL);"""

    def party_create(self, partyname, hqaddress, logourl):
        conn = init_db(self.party_table)
        cur = conn.cursor()
        cur.execute(""" INSERT INTO parties (party_name, hqAddress, logoUrl)
        VALUES('{}','{}','{}')
        RETURNING party_id, party_name; """.format(partyname, hqaddress, logourl))

        party = cur.fetchone()
        conn.commit()
        conn.close()
        return party

    def party_get(self,id = None):
        conn = connection()
        cur = conn.cursor()
        if id:
            cur.execute(""" SELECT party_id, party_name, logoUrl FROM parties WHERE party_id = '{}'; """.format(id))
            party = cur.fetchall()
            conn.close()
            data = {
                "party_id": party[0][0],
                "party_name" : party[0][1],
                "logoUrl": party[0][2]
                }
            return data

        else:
            cur.execute(""" SELECT party_id, party_name, logoUrl FROM parties ; """)
            parties = cur.fetchall()
            conn.close()
            data = []
            for party in parties:
                party = {
                    "party_id": party[0],
                    "party_name": party[1],
                    "logoUrl": party[2]
                }

                data.append(party)
            return data

    def party_exists(self, id):
        conn = connection()
        cur = conn.cursor()
        cur.execute(""" SELECT party_id from parties WHERE party_id = '{}' """.format(id))
        exist = cur.fetchall()
        conn.close()
        return exist  
    
    def party_edit(self, id, name):
        conn = connection()
        cur = conn.cursor()
        cur.execute(""" UPDATE parties SET party_name = '{}' WHERE party_id = '{}' ;""".format(name, id))
        conn.commit()
        conn.close()
        party = Parties().party_get(id)
        return party

    def party_delete(self, id):
        conn = connection()
        cur = conn.cursor()
        cur.execute(""" DELETE FROM parties WHERE party_id = '{}' ;""".format(id))
        conn.commit()
        conn.close()

    def party_name_exists(self, name):
        conn = connection()
        cur = conn.cursor()
        cur.execute(""" SELECT party_name from parties WHERE party_name = '{}' """.format(name))
        exit = cur.fetchall()
        conn.close()
        return exit
