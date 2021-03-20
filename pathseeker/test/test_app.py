import unittest

import pathseeker.src.app as app


class TestApp(unittest.TestCase):
    def test_app_created(self):
        application = app.APP.test_client()
        self.assertIsNotNone(application)

    def test_db_created(self):
        database = app.DATABASE
        self.assertIsNotNone(database)
