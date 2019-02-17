"""
Tests for Users
"""
import json
from app import create_app
from unittest import TestCase
from app.api_2.models.candidate_models import Candidates
from app.api_2.models.connection import connection
from app.api_2.models.db_config import destroy_db
class TestCandidates(TestCase):
    """
    Test v2 Candidates view 
    """
    def setUp(self):
        destroy_db()
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.candidate = {
            "user_id": 1,
            "party_id": 2
            }

        self.response = self.client.post('/api/v2/office/1/register', json=self.candidate)

    def tearDown(self):
            self.app = None
            self.client = None
            conn = connection()
            cur = conn.cursor()
            cur.execute(""" DELETE FROM candidates""")
            conn.commit()
            conn.close()

    
    