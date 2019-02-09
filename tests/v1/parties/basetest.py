import unittest
import os
import requests
import json
from app import create_app


class BaseTest(unittest.TestCase):
    """ Base Class for testing Parties Endpoint """

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.response = self.client.post('/api/v1/parties', headers={'Content-Type':'application/json'}, data=json.dumps(self.data))
        
    def tareDown(self):
        self.app = None

