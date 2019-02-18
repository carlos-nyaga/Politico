"""
Tests for Political Parties
"""
import os
from app import create_app
from unittest import TestCase
from app.api_2.models.party_models import Parties
from app.api_2.models.db_config import destroy_db


class TestPoliticalParties(TestCase):
    """
    Test Political Party Views 
    """
    def setUp(self):
        destroy_db()
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.political_party = {
            "party_name": "ODM",
            "hqAddress": "Nairobi",
            "logoUrl": "http://image.png"
            }

    def tearDown(self):
        destroy_db()
        self.app = None
        self.client = None
        

    
    def test_party_created_status_code(self):
        """
        Test Political Parties create
        """
        response = self.client.post('/api/v2/parties', json=self.political_party)
        self.assertEqual(response.status_code, 201)
    
    def test_party_created_data(self):
        response = self.client.post('/api/v2/parties', json=self.political_party)
        self.assertIn("ODM", str(response.data))
        

    def test_party_created_id_data_key(self):
        response = self.client.post('/api/v2/parties', json=self.political_party)
        self.assertIn("party_id", str(response.data))
    
    def test_present_name_data_key(self):
        response = self.client.post('/api/v2/parties', json=self.political_party)
        self.assertIn("party_name", str(response.data))
    
    def test_party_hqaddress_data_key(self):
        response = self.client.post('/api/v2/parties', json=self.political_party)
        self.assertNotIn("hqAddress", str(response.data), msg="hqAddress should not be in response")

    def test_party_logourl_data_key(self):
        response = self.client.post('/api/v2/parties', json=self.political_party)
        self.assertNotIn("logoUrl", str(response.data), msg="logoUrl should not be in response")

    def test_party_name_response_(self):
        Parties().party_create("Damiun", "Nakuru", "shutter.com")
        response = self.client.get('/api/v2/parties')
        self.assertIn('Damiun', str(response.data))
        

    def test_get_political_parties(self):
        """
        Test Political Parties get
        """
        Parties().party_create(
        "D0p3", "Nakuru", "shutterspeeed.com")
        response = self.client.get('/api/v2/parties')
        self.assertEqual(response.status_code, 200)
        self.assertIn('D0p3', str(response.data))

    def test_get_id_data_key(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.get('/api/v2/parties')
        self.assertIn("party_id", str(response.data))

    def test_get_logourl_data_key(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.get('/api/v2/parties')
        self.assertIn("logoUrl", str(response.data))
    
    def test_get_hqaddress_data_key(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.get('/api/v2/parties')
        self.assertNotIn("hqAddress", str(response.data), msg="hqAddress should not be in response")




    def test_get_specific_party_return_data(self):
        """
        Test Specific Political Parties get
        """
        Parties().party_create(
        "partyone", "SA", "exom.kkp"
        )

        Parties().party_create(
        "partytwo", "AS", "ee.com"
        )

        response = self.client.get('/api/v2/parties/2')
        self.assertIn('partytwo', str(response.data))

    def test_get_specific_party_status_code(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.get('/api/v2/parties/1')
        self.assertEqual(response.status_code, 200)

    def test_get_error_response(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.get('/api/v2/parties/5')
        self.assertEqual(response.status_code, 404)

    def test_get_specifig_id_data_key(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.get('/api/v2/parties/1')
        self.assertIn("party_id", str(response.data))

    def test_get_specific_logourl_data_key(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.get('/api/v2/parties/1')
        self.assertIn("logoUrl", str(response.data))
    
    def test_get_specific_hqaddress_data_key(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.get('/api/v2/parties/1')
        self.assertNotIn("hqAddress", str(response.data), msg="hqAddress should not be in response")

    


    def test_edit_polotical_party(self):
        """
        Test Edit Specific Political Parties get
        """
        Parties().party_create(
        "partybefore", "AS", "ee.com"
        )
        editted_party_data = {
            "party_name": "partyafter"}

        response = self.client.patch('/api/v2/parties/1', json=editted_party_data)
        self.assertIn('partyafter', str(response.data))

    def test_edit_status_code(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        edit = {
            "party_name": "donateam"
        }
        response = self.client.patch(
        '/api/v2/parties/1', json=edit)
        self.assertEqual(response.status_code, 200)

    def test_party_name_change(self):
        Parties().party_create(
        "D3m0part", "AS", "ee.com"
        )
        edit = {
            "party_name": "D3m0t3am"
        }
        response = self.client.patch('/api/v2/parties/1', json=edit)
        response = self.client.get('/api/v2/parties/1')
        self.assertNotIn('D3m0part', str(response.data))

    def test_edit_error_response(self):
        edit = {
            "name": "donateam"
        }
        response = self.client.patch('/api/v2/parties/7', json=edit)
        self.assertEqual(response.status_code, 404)

    def test_delete_party_status_code(self):
        """
        Test Delete Specific Political Parties get
        """
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.delete('/api/v2/parties/1' )
        self.assertEqual(response.status_code, 200)

    def test_delete_party(self):
        Parties().party_create("Sample Get", "Some Address", "example.com")
        response = self.client.delete('/api/v2/parties/1' )
        self.assertNotIn('Sample Get', str(response.data))

        