import string
import unittest

import hypothesis
import hypothesis.strategies as strategies

import pathseeker.src.ability as ability


class TestAbility(unittest.TestCase):
    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_get_name(self, name: str, short_name: str):
        test_ability = ability.Ability(name=name, short_name=short_name)
        self.assertEqual(test_ability.name, name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_get_short_name(self, name: str, short_name: str):
        test_ability = ability.Ability(name=name, short_name=short_name)
        self.assertEqual(test_ability.short_name, short_name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_str(self, name: str, short_name: str):
        test_ability = ability.Ability(name=name, short_name=short_name)
        self.assertEqual(
            str(test_ability), f"Ability: name={name}, short_name={short_name}"
        )
