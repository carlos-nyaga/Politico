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

    def tearDown(self):
            self.app = None
            self.client = None
            destroy_db()

    def test_party_created_status_code(self):
        """
        Test User create
        """
        response = self.client.post(
        '/api/v2/auth/signup', json=self.new_user)
        self.assertIn("John", str(response.data))

    def test_party_created_id_data_key(self):
        response = self.client.post(
        '/api/v2/auth/signup', json=self.new_user)
        self.assertIn("id", str(response.data))
    
    def test_party_created_email_data_key(self):
        response = self.client.post(
        '/api/v2/auth/signup', json=self.new_user)
        self.assertIn("email", str(response.data))
    
    def test_party_created_fname_data_key(self):
        response = self.client.post(
        '/api/v2/auth/signup', json=self.new_user)
        self.assertIn("first_name", str(response.data))
    
    def test_party_created_isadmin_data_key(self):
        response = self.client.post(
        '/api/v2/auth/signup', json=self.new_user)
        self.assertIn("isadmin", str(response.data))
        
    def test_party_created_token_data_key(self):
        response = self.client.post(
        '/api/v2/auth/signup', json=self.new_user)
        self.assertIn("token", str(response.data))
    
    def test_party_password_data_key(self):
        response = self.client.post(
        '/api/v2/auth/signup', json=self.new_user)
        self.assertNotIn("password", str(response.data), msg="password should not be in response")

    def test_encode_auth_token(self):
        token = (Users().auth_token_encode(1))
        self.assertTrue(isinstance(token, bytes))
        