import string
import typing
import unittest

import hypothesis
import hypothesis.strategies as strategies

from pathseeker.src.data_types.ability import Ability
from pathseeker.test.common.test_data_type_base import TestDataType


class TestAbility(unittest.TestCase, TestDataType):
    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_get_name(self, name: str, short_name: str):
        test_ability = Ability(name=name, short_name=short_name)
        self.assertEqual(test_ability.name, name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_get_short_name(self, name: str, short_name: str):
        test_ability = Ability(name=name, short_name=short_name)
        self.assertEqual(test_ability.short_name, short_name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_str(self, name: str, short_name: str):
        test_ability = Ability(name=name, short_name=short_name)
        self.assertEqual(str(test_ability), f"Ability: name={name}, short_name={short_name}")

    @hypothesis.given(abilities=strategies.lists(Ability.strategy(), unique=True, min_size=2, max_size=2))
    def test_eq_different_abilities(self, abilities: typing.List[Ability]):
        self.assertEqual(abilities[0], abilities[1])

    @hypothesis.given(ability=Ability.strategy())
    def test_eq_same_abilities(self, ability: Ability):
        self.assertEqual(ability, ability)
