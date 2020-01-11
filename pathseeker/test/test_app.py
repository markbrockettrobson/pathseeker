import unittest

import flask

import pathseeker.src.app as app


class TestAtLeastAPI(unittest.TestCase):

    def test_app_created(self):
        app.APP.test_client()
