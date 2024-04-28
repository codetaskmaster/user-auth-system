from unittest import TestCase
from app import create_app
from instance.config import TestingConfig
from app.api.db import Connection


class BaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig())
        self.client = self.app.test_client()
        conn = Connection()
        conn.create_table()

    def register(self, data):
        """register user method"""
        return self.client.post(
            "api/v1/register", data=data, content_type="application/json"
        )

    def login(self, data):
        """login user method"""
        return self.client.post(
            "api/v1/login", data=data, content_type="application/json"
        )

    def tearDown(self):
        with self.app.app_context():
            conn = Connection()
            conn.drop_table()