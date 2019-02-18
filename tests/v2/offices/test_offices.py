"""
Tests for Political Offices
"""

from app import create_app
from unittest import TestCase
from app.api_2.models.offices_models import Offices
from app.api_2.models.db_config import destroy_db


class TestPoliticalOffices(TestCase):
    """
    Test Political Party Views 
    """
    def setUp(self):
        destroy_db()
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.political_office = {
            "office_name": "President",
            "office_type": "State"
            }
        self.db = Offices()

    def tearDown(self):
        destroy_db()
        self.app = None
        self.client = None
          

    
    def test_office_created_status_code(self):
        """
        Test Political Offices create
        """
        response = self.client.post('/api/v2/offices', json=self.political_office)
        self.assertEqual(response.status_code, 201)

    def test_office_created_data(self):
        response = self.client.post('/api/v2/offices', json=self.political_office)
        self.assertIn("President", str(response.data))
        

    def test_office_created_id_data_key(self):
        response = self.client.post(
        '/api/v2/offices', json=self.political_office)
        self.assertIn("office_id", str(response.data))
    
    def test_present_name_data_key(self):
        response = self.client.post(
        '/api/v2/offices', json=self.political_office)
        self.assertIn("office_name", str(response.data))
    
    def test_offices_type_data_key(self):
        office = {"name":"Tano5", "type":"State"}
        response = self.client.post(
        '/api/v2/offices', json=office)
        self.assertIn("office_type", str(response.data), msg="type should be in response")


    def test_offices_name_response_(self):
        Offices().office_create("Tano5", "State")
        response = self.client.get('/api/v2/offices')
        self.assertIn('Tano5', str(response.data))
      

    def test_get_political_offices(self):
        """
        Test Political Offices get
        """
        self.db.office_create(
        "D0p3", "local government")
        response = self.client.get('/api/v2/offices')
        self.assertEqual(response.status_code, 200)
        self.assertIn('D0p3', str(response.data))

    def test_get_id_data_key(self):
        Offices().office_create(
        "Paclo", "executive"
        )
        response = self.client.get('/api/v2/offices')
        self.assertIn("office_id", str(response.data))

    def test_get_logourl_data_key(self):
        Offices().office_create(
        "Paclo", "executive"
        )
        response = self.client.get('/api/v2/offices')
        self.assertIn("office_name", str(response.data))

    def test_get_type_data_key(self):
        Offices().office_create(
        "Paclo", "executive"
        )
        response = self.client.get('/api/v2/offices')
        self.assertIn("office_type", str(response.data), msg="type should be in response")




    def test_get_specific_offices_return_data(self):
        """
        Test Specific Political Office get
        """
        self.db.office_create(
        "Paclo", "executive"
        )

        self.db.office_create(
        "officestwo", "local"
        )

        response = self.client.get('/api/v2/offices/2')
        self.assertIn('officestwo', str(response.data))

    def test_get_specific_offices_status_code(self):
        Offices().office_create(
        "Paclo", "executive"
        )
        response = self.client.get('/api/v2/offices/1')
        self.assertEqual(response.status_code, 200)

    def test_get_error_response(self):
        Offices().office_create(
        "Paclo", "executive"
        )
        response = self.client.get('/api/v2/offices/5')
        self.assertEqual(response.status_code, 404)

    def test_get_specifig_id_data_key(self):
        Offices().office_create(
        "Paclo", "executive"
        )
        response = self.client.get('/api/v2/offices/1')
        self.assertIn("office_id", str(response.data))

    def test_get_specific_logourl_data_key(self):
        Offices().office_create(
        "Paclo", "executive"
        )
        response = self.client.get('/api/v2/offices/1')
        self.assertIn("office_name", str(response.data))
    
    def test_get_specific_hqaddress_data_key(self):
        Offices().office_create(
        "Paclo", "executive"
        )
        response = self.client.get('/api/v2/offices/1')
        self.assertIn("office_type", str(response.data), msg="office_type should be in response")
