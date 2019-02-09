"""
Tests for Political Offices
"""

from app import create_app
from unittest import TestCase
from app.api_1.models.offices_models import Offices



class TestOfficessViews(TestCase):
  """
  Test Political Offices Views
  """
  def setUp(self):
      self.app = create_app(config_name=('testing'))
      self.client = self.app.test_client()
      self.political_office = {
          "name": "Chief",
            "type": "local government"
        }

  def test_get_polotical_office(self):
    """
    Test Political Offices GET
    """
    Offices().office_create(
      "Sample Get", "Presidential")
    response = self.client.get('/api/v1/office')
    retrieved_political_offices = response.data
    self.assertEqual(response.status_code, 200)
    self.assertIn('Sample Get', str(response.data))

  def test_office_create(self):
    """
    Test Political Offices Create
    """
    response = self.client.post(
      '/api/v1/office', json=self.political_office)
    self.assertEqual(response.status_code, 200)
    response = self.client.get('/api/v1/office')
    self.assertEqual(response.status_code, 200)
    self.assertIn('Sample', str(response.data))

  def test_get_specific_political_office(self):
    """
    Test Political Offices Get Specific
    """
    Offices().office_create(
      "Sample 1", "Presidential"
    )

    political_office= Offices().office_create(
      "Sample 2", "Presidential"
    )

    response = self.client.get('/api/v1/office/' + str(political_office['id']))

    self.assertIn('Sample 2', str(response.data))
    self.assertNotIn('Sample 1', str(response.data))