import uuid
from django.test import TestCase
from amicci_app.models import Vendor

class TestApiSetup(TestCase):

    def setUp(self):
        self.vendor = Vendor.objects.create(
            name='test_vendor_{}'.format(uuid.uuid4()),
        )
