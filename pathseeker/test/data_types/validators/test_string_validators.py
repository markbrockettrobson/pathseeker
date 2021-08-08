from string import ascii_letters, ascii_lowercase, ascii_uppercase
from typing import Set
from unittest import TestCase

from hypothesis import assume, given
from hypothesis.strategies import sets, text

from pathseeker.src.data_types.validators.string_validators import (
    cant_be_empty,
    must_be_lowercase,
    must_be_uppercase,
    string_value_in_collection,
)


class TestStringValidators(TestCase):
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

    @given(values=sets(text(min_size=1), min_size=1, max_size=10))
    def test_string_value_in_collection(self, values: Set[str]):
        validator = string_value_in_collection(values)
        for value in values:
            self.assertEqual(value, validator(value))

    @given(values=sets(text(min_size=1), min_size=1, max_size=10), value=text(min_size=1))
    def test_string_value_in_collection_error(self, values: Set[str], value: str):
        assume(value not in values)
        validator = string_value_in_collection(values)
        with self.assertRaises(ValueError):
            validator(value)
