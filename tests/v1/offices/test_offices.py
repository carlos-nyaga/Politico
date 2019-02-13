"""
Tests for Political Offices
"""

from app import create_app
from unittest import TestCase
from app.api_1.models.offices_models import Offices


class TestPoliticalOffices(TestCase):
    """
    Test Political Party Views 
    """
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.political_office = {
            "name": "HP32456",
            "type": "Nair3obi4"
            }
        self.db = Offices()

    def tearDown(self):
            self.app = None
            self.client = None
            self.political_office = {}

    
    def test_office_created_status_code(self):
        """
        Test Political Offices create
        """
        self.political_office = {
            "name": "Deputy",
            "type": "state"}
        response = self.client.post(
        '/api/v1/offices', json=self.political_office)
        self.assertIn("Deputy", str(response.data))
        

    def test_office_created_id_data_key(self):
        response = self.client.post(
        '/api/v1/offices', json=self.political_office)
        self.assertIn("id", str(response.data))
    
    def test_present_name_data_key(self):
        response = self.client.post(
        '/api/v1/offices', json=self.political_office)
        self.assertIn("name", str(response.data))
    
    def test_offices_type_data_key(self):
        office = {"name":"Tano5", "type":"State"}
        response = self.client.post(
        '/api/v1/offices', json=office)
        self.assertIn("type", str(response.data), msg="type should be in response")


    def test_offices_name_response_(self):
        Offices().office_create("Tano5", "State")
        response = self.client.get('/api/v1/offices')
        self.assertIn('Tano5', str(response.data))
      

    def test_get_political_offices(self):
        """
        Test Political Offices get
        """
        self.db.office_create(
        "D0p3", "local government")
        response = self.client.get('/api/v1/offices')
        self.assertEqual(response.status_code, 200)
        self.assertIn('D0p3', str(response.data))

    def test_get_id_data_key(self):
        response = self.client.get('/api/v1/offices')
        self.assertIn("id", str(response.data))

    def test_get_logourl_data_key(self):
        response = self.client.get('/api/v1/offices')
        self.assertIn("name", str(response.data))

    def test_get_type_data_key(self):
        response = self.client.get('/api/v1/offices')
        self.assertIn("type", str(response.data), msg="type should be in response")




    def test_get_specific_offices_return_data(self):
        """
        Test Specific Political Office get
        """
        self.db.office_create(
        "Paclo", "executive"
        )

        office2 = self.db.office_create(
        "officestwo", "local"
        )

        response = self.client.get('/api/v1/offices/{}'.format(office2['office_id']))
        self.assertIn('officestwo', str(response.data))

    def test_get_specific_offices_status_code(self):
        response = self.client.get('/api/v1/offices/1')
        self.assertEqual(response.status_code, 200)

    def test_get_error_response(self):
        response = self.client.get('/api/v1/offices/5')
        self.assertEqual(response.status_code, 404)

    def test_get_specifig_id_data_key(self):
        response = self.client.get('/api/v1/offices/1')
        self.assertIn("id", str(response.data))

    def test_get_specific_logourl_data_key(self):
        response = self.client.get('/api/v1/offices/1')
        self.assertIn("name", str(response.data))
    
    def test_get_specific_hqaddress_data_key(self):
        response = self.client.get('/api/v1/offices/1')
        self.assertIn("type", str(response.data), msg="typeshould be in response")
