from string import ascii_letters, ascii_lowercase, ascii_uppercase
from unittest import TestCase

from hypothesis import given
from hypothesis.strategies import text

from pathseeker.src.data_types.validators.string_validators import cant_be_empty, must_be_lowercase, must_be_uppercase


class TestApp(TestCase):
    def test_cant_be_empty_empty_string(self):
        with self.assertRaises(ValueError):
            cant_be_empty("")

    @given(value=text(alphabet=ascii_letters, min_size=1))
    def test_cant_be_non_empty_empty_string(self, value: str):
        self.assertEqual(value, cant_be_empty(value))

    @given(value=text(alphabet=ascii_lowercase, min_size=1))
    def test_must_be_uppercase_lower(self, value: str):
        with self.assertRaises(ValueError):
            must_be_uppercase(value)

    @given(value=text(alphabet=ascii_uppercase, min_size=1))
    def test_must_be_uppercase_upper(self, value: str):
        self.assertEqual(value, must_be_uppercase(value))

    @given(value=text(alphabet=ascii_uppercase, min_size=1))
    def test_must_be_lowercase_upper(self, value: str):
        with self.assertRaises(ValueError):
            must_be_lowercase(value)

    @given(value=text(alphabet=ascii_lowercase, min_size=1))
    def test_must_be_lowercase_lower(self, value: str):
        self.assertEqual(value, must_be_lowercase(value))
