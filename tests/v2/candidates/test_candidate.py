"""
Tests for Users
"""
import json
from app import create_app
from unittest import TestCase
from app.api_2.models.candidate_models import Candidates
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
            "party_id": 1
            }
        self.user = {
            "first_name": "John",
            "last_name": "Doe",
            "other_name": "Jane",
            "email": "john@janedoe.com",
            "phone_number": "7283747481",
            "passport_url": "https//:passort.com",
            "password": "password",
            "isadmin": "True" 
            }
        self.office= {
            "office_name": "President",
            "office_type": "State"
            }
        self.party = {
            "party_name": "ODM",
            "hqAddress": "Nairobi",
            "logoUrl": "http://image.png"
            }
        self.client.post('/api/v2/auth/signup', json=self.user)
        self.client.post('/api/v2/offices', json=self.office)
        self.client.post('/api/v2/parties', json=self.party)
        self.response = self.client.post('/api/v2/office/1/register', json=self.candidate)

    def tearDown(self):
            self.app = None
            self.client = None
            destroy_db()

    def test_candidate_created_status_code(self):
        """
        Test Candidate register
        """
        self.assertEqual(self.response.status_code, 201)

    def test_candidate_created_candidate_id_data_key(self):
        self.assertIn("candidate_id", str(self.response.data))

    def test_candidate_created_office_id_data_key(self):
        self.assertIn("office_id", str(self.response.data))
    
    def test_candidate_created_party_id_data_key(self):
        self.assertNotIn("party_id", str(self.response.data))
    
    def test_candidate_created_msg_data_key(self):
        self.assertIn("msg", str(self.response.data))
        
    
    
    
    