import unittest
import os
import requests
import json
from app import create_app
from tests.v1.parties.basetest import BaseTest

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

    def payload(self):
        return {
            "name": self.name,
            "hqAddress": self.hqaddress,
            "logoUrl": self.logourl
        }
    def test_should_return_expected_status_code(self):
            self.assertEqual(self.response.status, self.expected_status_code)

    def test_should_return_expected_payload(self):
        self.assertEqual(self.response.data(), self.expected_return_payload)


if __name__ == '__main__':
    unittest.main()