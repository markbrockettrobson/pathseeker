from unittest import TestCase

from pathseeker.src.app import APP, DATABASE


class TestApp(TestCase):
    def test_app_created(self):
        application = APP.test_client()
        self.assertIsNotNone(application)

    def test_db_created(self):
        database = DATABASE
        self.assertIsNotNone(database)
