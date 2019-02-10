"""
Tests for Political Parties
"""
from flask import jsonify
import os
from app import create_app
from unittest import TestCase
from app.api_1.models.parties_models import Parties


class TestPoliticalParties(TestCase):
    """
    Test Political Party Views 
    """
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.political_party = {
            "name": "HP32456",
            "hqAddress": "Nair3obi4",
            "logoUrl": "http://tes4t.image.jpg"}

    def tearDown(self):
            self.app = None
            self.client = None
            self.political_party = {}

    
    def test_party_created_status_code(self):
        """
        Test Political Parties create
        """
        self.political_party = {
            "name": "LastOne",
            "hqAddress": "N3obi4",
            "logoUrl": "http://s4t.image.jpg"}
        response = self.client.post(
        '/api/v1/parties', json=self.political_party)
        self.assertIn("LastOne", str(response.data))
        

    def test_party_created_id_data_key(self):
        response = self.client.post(
        '/api/v1/parties', json=self.political_party)
        self.assertIn("id", str(response.data))
    
    def test_present_name_data_key(self):
        response = self.client.post(
        '/api/v1/parties', json=self.political_party)
        self.assertIn("name", str(response.data))
    
    def test_party_hqaddress_data_key(self):
        response = self.client.post(
        '/api/v1/parties', json=self.political_party)
        self.assertNotIn("hqAddress", str(response.data), msg="hqAddress should not be in response")

    def test_party_logourl_data_key(self):
        response = self.client.post(
        '/api/v1/parties', json=self.political_party)
        self.assertNotIn("logoUrl", str(response.data), msg="logoUrl should not be in response")

    def test_party_name_response_(self):
        Parties().party_create("Damiun", "Nakuru", "shutter.com")
        response = self.client.get('/api/v1/parties')
        self.assertIn('Damiun', str(response.data))
        

    def test_get_political_parties(self):
        """
        Test Political Parties get
        """
        Parties().party_create(
        "D0p3", "Nakuru", "shutterspeeed.com")
        response = self.client.get('/api/v1/parties')
        self.assertEqual(response.status_code, 200)
        self.assertIn('D0p3', str(response.data))

    def test_get_id_data_key(self):
        response = self.client.get('/api/v1/parties')
        self.assertIn("id", str(response.data))

    def test_get_logourl_data_key(self):
        response = self.client.get('/api/v1/parties')
        self.assertIn("logoUrl", str(response.data))
    
    def test_get_hqaddress_data_key(self):
        response = self.client.get('/api/v1/parties')
        self.assertNotIn("hqAddress", str(response.data), msg="hqAddress should not be in response")




    def test_get_specific_party_return_data(self):
        """
        Test Specific Political Parties get
        """
        Parties().party_create(
        "partyone", "SA", "exom.kkp"
        )

        party2 = Parties().party_create(
        "partytwo", "AS", "ee.com"
        )

        response = self.client.get('/api/v1/parties/{}'.format(party2['party_id']))
        self.assertIn('partytwo', str(response.data))

    def test_get_specific_party_status_code(self):
        response = self.client.get('/api/v1/parties/1')
        self.assertEqual(response.status_code, 200)

    def test_get_error_response(self):
        response = self.client.get('/api/v1/parties/5')
        self.assertEqual(response.status_code, 404)

    def test_get_specifig_id_data_key(self):
        response = self.client.get('/api/v1/parties/1')
        self.assertIn("id", str(response.data))

    def test_get_specific_logourl_data_key(self):
        response = self.client.get('/api/v1/parties/1')
        self.assertIn("logoUrl", str(response.data))
    
    def test_get_specific_hqaddress_data_key(self):
        response = self.client.get('/api/v1/parties/1')
        self.assertNotIn("hqAddress", str(response.data), msg="hqAddress should not be in response")

    


    def test_edit_polotical_party(self):
        """
        Test Edit Specific Political Parties get
        """
        partyedit= Parties().party_create(
        "partybefore", "AS", "ee.com"
        )
        editted_party_data = {
            "name": "partyafter"}

        response = self.client.patch('/api/v1/parties/{}'.format(partyedit['party_id']), json=editted_party_data)
        self.assertIn('partyafter', str(response.data))

    def test_edit_status_code(self):
        edit = {
            "name": "donateam"
        }
        response = self.client.patch(
        '/api/v1/parties/3', json=edit)
        self.assertEqual(response.status_code, 200)

    def test_party_name_change(self):
        partyedit= Parties().party_create(
        "D3m0part", "AS", "ee.com"
        )
        edit = {
            "name": "D3m0t3am"
        }
        response = self.client.patch('/api/v1/parties/{}'.format(partyedit["party_id"]), json=edit)
        response = self.client.get('/api/v1/parties')
        self.assertNotIn('D3m0part', str(response.data))

    def test_edit_error_response(self):
        edit = {
            "name": "donateam"
        }
        response = self.client.patch('/api/v1/parties/7', json=edit)
        self.assertEqual(response.status_code, 404)

    def test_delete_party_status_code(self):
        """
        Test Edit Specific Political Parties get
        """
        party = Parties().party_create(
        "Sample Get", "Some Address", "example.com")
 

        response = self.client.delete('/api/v1/parties/{}'.format(party["party_id"]) )
        self.assertEqual(response.status_code, 200)

    def test_delete_party(self):
        party = Parties().party_create(
        "Sample Get", "Some Address", "example.com")
        response = self.client.delete('/api/v1/parties/{}'.format(party["party_id"]) )
        self.assertNotIn('Sample Get', str(response.data))

        