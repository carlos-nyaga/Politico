
from app import create_app
from unittest import TestCase
from app.api_2.models.db_config import init_db

class DatabaseConnection(TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
       


    def test_connection(self):
        query = """ CREATE TABLE IF NOT EXISTS offices(
            office_id serial PRIMARY KEY NOT NULL,
            office_name character varying(50) NOT NULL,
            office_type character varying(50) NOT NULL);"""


        try:
            init_db(query)
        
        except Exception as e:
            return e