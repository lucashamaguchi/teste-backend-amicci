from amicci_app.tests.test_setup import TestApiSetup
from rest_framework import status
import json


class TestMyModelLogAPIs(TestApiSetup):
    def test_get_all_my_model(self):
        response = self.client.get('/api/vendors/')
        print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content_json = json.loads(response.content.decode('utf-8'))
        self.assertEqual('test_vendor_' in content_json['results'][0]['name'], True)

    # Add more integration tests for other endpoints and functionalities
