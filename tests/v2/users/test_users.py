"""
Tests for Users
"""
import os ,json, objectpath
from app import create_app
from unittest import TestCase
from app.api_2.models.db_config import destroy_db
from app.api_2.models.user_models import Users

class TestUsers(TestCase):
    """
    Test v2 Users view 
    """
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.new_user = {
            "first_name": "John",
            "last_name": "Doe",
            "other_name": "Jane",
            "email": "john@janedoe.com",
            "phone_number": "7283747481",
            "passport_url": "https//:passort.com",
            "password": "password",
            "isadmin": "True" 
            }
        self.login_user = {
            "email": "john@janedoe.com",
            "password": "password"
            }
        self.response = self.client.post('/api/v2/auth/signup', json=self.new_user)


    def tearDown(self):
            self.app = None
            self.client = None
            destroy_db()

    def test_user_created_status_code(self):
        """
        Test User create
        """
        self.assertIn("John", str(self.response.data))

    def test_user_created_id_data_key(self):
        self.assertIn("id", str(self.response.data))

    def test_user_created_email_data_key(self):
        self.assertIn("email", str(self.response.data))
    
    def test_user_created_fname_data_key(self):
        self.assertIn("first_name", str(self.response.data))
    
    def test_user_created_isadmin_data_key(self):
        self.assertIn("isadmin", str(self.response.data))
        
    def test_user_created_token_data_key(self):
        self.assertIn("token", str(self.response.data))
    
    def test_user_password_data_key(self):
        self.assertNotIn("password", str(self.response.data), msg="password should not be in response")

    def test_encode_auth_token(self):
        token = (Users().auth_token_encode(1))
        self.assertTrue(isinstance(token, bytes))
        
    
    def test_user_login_status_code(self):
        """
        Test User login
        """
        response = self.client.post('/api/v2/auth/login', json=self.login_user)
        self.assertIn("John", str(response.data))

    def test_user_login_id_data_key(self):
        response = self.client.post('/api/v2/auth/login', json=self.login_user)
        self.assertIn("id", str(response.data))
    
    def test_user_login_email_data_key(self):
        response = self.client.post('/api/v2/auth/login', json=self.login_user)
        self.assertIn("email", str(response.data))
    
    def test_user_login_fname_data_key(self):
        response = self.client.post('/api/v2/auth/login', json=self.login_user)
        self.assertIn("first_name", str(response.data))
    
    def test_user_login_isadmin_data_key(self):
        response = self.client.post('/api/v2/auth/login', json=self.login_user)
        self.assertIn("isadmin", str(response.data))
        
    def test_user_login_token_data_key(self):
        response = self.client.post('/api/v2/auth/login', json=self.login_user)
        self.assertIn("token", str(response.data))
    
    def test_user_logn_password_data_key(self):
        response = self.client.post('/api/v2/auth/login', json=self.login_user)
        self.assertNotIn("password", str(response.data), msg="password should not be in response")