import unittest
import os
import requests
import json
from app import create_app




class BaseTest(unittest.TestCase):
    """ Base Class for testing Parties Endpoint """

    def payload(self):
        return {
            "name": self.name,
            "hqAddress": self.hqaddress,
            "logoUrl": self.logourl
        }
    
    expected_status_code = 200
    expected_return_payload = {}


    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.response = self.client.post('/api/v1{}'.format(self.path), headers={'Content-Type':'application/json'}, data=json.dumps(payload))
        
    def test_should_return_expected_status_code(self):
        self.assertEqual(self.response.status, self.expected_status_code)

    def test_should_return_expected_payload(self):
        self.assertEqual(self.response.data(), self.expected_return_payload)

    def tareDown(self):
        self.app = None



class TestParties(BaseTest):
    """docstring for TestingParties"""
    path ="/parties"
    name = "NASA"
    hqaddress = "Nairobi"
    logourl = "https://nasa.co.ke/icon.png"
    expected_status_code = 200
    expected_return_payload = {
        "id": 4,
        "hqAddress": "Nairobi",
        "logoUrl" : "https://nasa.co.ke/icon.png" 
    }


if __name__ == '__main__':
    unittest.main()