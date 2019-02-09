"""
Tests for Political Parties
"""
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
            "name": "DRK5ID3",
            "hqAddress": "Nairobi",
            "logoUrl": "http://test.image.jpg"}
    
    def test_party_created_status_code(self):
        """
        Test Political Parties create
        """
        response = self.client.post(
        '/api/v1/parties', json=self.political_party)
        self.assertEqual(response.status_code, 200)
        

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
        

    def test_get_polotical_parties(self):
        """
        Test Political Parties get
        """
        Parties().party_create(
        "Team", "Nakuru", "shutterspeeed.com")
        response = self.client.get('/api/v1/parties')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Damiun', str(response.data))



    def test_get_specific_office_return_data(self):
        """
        Test Political Offices Get Specific
        """
        Parties().party_create(
        "anc", "SA", "exom.kkp"
        )

        political_party = Parties().party_create(
        "can", "AS", "ee.com"
        )

        response = self.client.get('/api/v1/parties/' + str(political_party['party_id']))
        self.assertIn('can', str(response.data))

    def test_get_specific_office_return_true_data(self):
        """
        Test Political Offices Get Specific
        """
        Parties().party_create(
        "anc", "SA", "exom.kkp"
        )

        political_party = Parties().party_create(
        "can", "AS", "ee.com"
        )

        response = self.client.get('/api/v1/parties/' + str(political_party['party_id']))
        self.assertNotIn('anc', str(response.data))



    def test_edit_polotical_party(self):
        """
        Test Political Parties edit
        """
        political_party = Parties().party_create(
        "Sample", "Some Address", "example.com")
        response = self.client.get('/api/v1/parties')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sample Get', str(response.data))

        editted_party_data = {
            "name": "Sample Edit",
            "hqAddress": "Some Address",
            "logoUrl": "example.com"}

        response = self.client.patch(
        '/api/v1/parties/' + str(political_party['party_id']), json=editted_party_data)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/v1/parties')
        self.assertNotIn('Sample Get', str(response.data))
        self.assertIn('Sample Edit', str(response.data))

    def test_delete_polotical_party(self):
        """
        Test Political Parties delete
        """
        party = Parties().party_create(
        "Sample Get", "Some Address", "example.com")
        response = self.client.get('/api/v1/parties')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sample Get', str(response.data))

        self.client.delete('/api/v1/parties/' + party["party_id"])
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/api/v1/parties')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Sample Get', str(response.data))