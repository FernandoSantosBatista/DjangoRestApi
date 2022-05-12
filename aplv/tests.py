
from rest_framework.test import APIClient
from django.test import TestCase


class AplvTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_aplv_list(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_aplv_create(self):
        response = self.client.post('/register', {'name': 'test', 'district': 'test', 'city': 'test', 'email': 'test@gmail.com'}, format='json')
        self.assertEqual(response.status_code, 201)
   
    def test_aplv_getbyid(self):
        response = self.client.get('/register/{id}/', format='json')
        self.assertEqual(response.status_code, 200)