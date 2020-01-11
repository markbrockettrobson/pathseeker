import unittest

import pathseeker.src.app as app


class TestAtLeastAPI(unittest.TestCase):

    @staticmethod
    def test_app_created(self):
        app.APP.test_client()
