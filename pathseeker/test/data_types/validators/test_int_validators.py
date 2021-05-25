import unittest

import hypothesis
from hypothesis import strategies

from pathseeker.src.data_types.validators.int_validators import cant_be_negative, must_be_multiple_of_five


class TestApp(unittest.TestCase):
    @hypothesis.given(
        value=strategies.integers(max_value=-1),
    )
    def test_cant_be_negative_negative(self, value: int):
        with self.assertRaises(ValueError):
            cant_be_negative(value)

    @hypothesis.given(
        value=strategies.integers(min_value=0),
    )
    def test_cant_be_negative_positive(self, value: int):
        self.assertEqual(value, cant_be_negative(value))

    @hypothesis.given(multiple_of_five=strategies.integers(), error=strategies.integers(min_value=1, max_value=4))
    def test_must_be_multiple_of_five_negative(self, multiple_of_five: int, error: int):
        with self.assertRaises(ValueError, msg=f"Value sent {multiple_of_five*5 + error}"):
            must_be_multiple_of_five(multiple_of_five * 5 + error)

    @hypothesis.given(
        multiple_of_five=strategies.integers(),
    )
    def test_must_be_multiple_of_five_positive(self, multiple_of_five: int):
        self.assertEqual(
            multiple_of_five * 5, must_be_multiple_of_five(multiple_of_five * 5), msg=f"Value sent {multiple_of_five*5}"
        )
