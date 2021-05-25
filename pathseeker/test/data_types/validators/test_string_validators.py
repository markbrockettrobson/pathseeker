import string
import unittest

import hypothesis
from hypothesis import strategies

from pathseeker.src.data_types.validators.string_validators import cant_be_empty, must_be_lowercase, must_be_uppercase


class TestApp(unittest.TestCase):
    def test_cant_be_empty_empty_string(self):
        with self.assertRaises(ValueError):
            cant_be_empty("")

    @hypothesis.given(
        value=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_cant_be_non_empty_empty_string(self, value: str):
        self.assertEqual(value, cant_be_empty(value))

    @hypothesis.given(
        value=strategies.text(alphabet=string.ascii_lowercase, min_size=1),
    )
    def test_must_be_uppercase_lower(self, value: str):
        with self.assertRaises(ValueError):
            must_be_uppercase(value)

    @hypothesis.given(
        value=strategies.text(alphabet=string.ascii_uppercase, min_size=1),
    )
    def test_must_be_uppercase_upper(self, value: str):
        self.assertEqual(value, must_be_uppercase(value))

    @hypothesis.given(
        value=strategies.text(alphabet=string.ascii_uppercase, min_size=1),
    )
    def test_must_be_lowercase_upper(self, value: str):
        with self.assertRaises(ValueError):
            must_be_lowercase(value)

    @hypothesis.given(
        value=strategies.text(alphabet=string.ascii_lowercase, min_size=1),
    )
    def test_must_be_lowercase_lower(self, value: str):
        self.assertEqual(value, must_be_lowercase(value))
