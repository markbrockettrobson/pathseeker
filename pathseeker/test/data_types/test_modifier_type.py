import string
import unittest

import hypothesis
import hypothesis.strategies as strategies

from pathseeker.src.data_types.modifier_type import ModifierType


class TestModifierType(unittest.TestCase):
    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_get_name(self, name: str, short_name: str):
        test_ability = ModifierType(name=name, short_name=short_name)
        self.assertEqual(test_ability.name, name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_get_short_name(self, name: str, short_name: str):
        test_ability = ModifierType(name=name, short_name=short_name)
        self.assertEqual(test_ability.short_name, short_name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_str(self, name: str, short_name: str):
        test_ability = ModifierType(name=name, short_name=short_name)
        self.assertEqual(str(test_ability), f"ModifierType: name={name}, short_name={short_name}")
