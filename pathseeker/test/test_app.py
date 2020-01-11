import unittest

import pathseeker.src.app as app


class TestAtLeastAPI(unittest.TestCase):

    def test_app_created(self):
        application = app.APP.test_client()
        self.assertIsNotNone(application)
