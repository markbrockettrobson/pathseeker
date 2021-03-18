import random
import typing
import unittest
import unittest.mock as mock

import hypothesis
import hypothesis.strategies as strategies

from pathseeker.interface.data_types.i_ability import IAbility
from pathseeker.src.managers.ability_manager import AbilityManager

PATHFINDER_TYPES = [
    ("strength", "STR", AbilityManager.STRENGTH),
    ("dexterity", "DEX", AbilityManager.DEXTERITY),
    ("constitution", "CON", AbilityManager.CONSTITUTION),
    ("intelligence", "INT", AbilityManager.INTELLIGENCE),
    ("wisdom", "WIS", AbilityManager.WISDOM),
    ("charisma", "CHA", AbilityManager.CHARISMA),
    ("free", "FRE", AbilityManager.FREE),
]

NON_PATHFINDER_TYPES = [
    ("stregth", "STRENGTH", mock.create_autospec(IAbility)),
    ("1", "2", mock.create_autospec(IAbility)),
    ("WIS,CON", "dexterity", mock.create_autospec(IAbility)),
    ("CONSTITUTION", "con", mock.create_autospec(IAbility)),
]

ABILITY_SCORE_TO_ABILITY_MODIFIER = [
    (0, -5),
    (1, -5),
    (2, -4),
    (3, -4),
    (4, -3),
    (5, -3),
    (6, -2),
    (7, -2),
    (8, -1),
    (9, -1),
    (10, 0),
    (11, 0),
    (12, 1),
    (13, 1),
    (14, 2),
    (16, 3),
    (17, 3),
    (20, 5),
    (31, 10),
]


class TestAbilityManager(unittest.TestCase):
    def test_name_to_type_pathfinder_type(self):
        for name, _, ability_score_type in PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                returned_type = AbilityManager.name_to_type(name)
                self.assertEqual(returned_type, ability_score_type)

    def test_short_name_to_type_pathfinder_type(self):
        for _, short_name, ability_score_type in PATHFINDER_TYPES:
            with self.subTest(f"test: short_name={short_name}"):
                returned_type = AbilityManager.short_name_to_type(short_name)
                self.assertEqual(returned_type, ability_score_type)

    def test_name_to_type_non_pathfinder_type(self):
        for name, _, _ in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                with self.assertRaises(Exception) as exception:
                    AbilityManager.name_to_type(name)
                self.assertEqual(str(exception.exception), f'Unknown Ability name "{name}"')

    def test_short_name_to_type_non_pathfinder_type(self):
        for _, short_name, _ in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: short_name={short_name}"):
                with self.assertRaises(Exception) as exception:
                    AbilityManager.short_name_to_type(short_name)
                self.assertEqual(str(exception.exception), f'Unknown Ability short name "{short_name}"')

    @hypothesis.given(strategies.lists(strategies.integers(min_value=0, max_value=len(PATHFINDER_TYPES) - 1)))
    def test_comma_separated_name_list_to_type_list(self, test_index_list: typing.List[int]):
        type_list = [PATHFINDER_TYPES[index][2] for index in test_index_list]
        test_str = ",".join([PATHFINDER_TYPES[index][0] for index in test_index_list])
        self.assertListEqual(type_list, AbilityManager.comma_separated_name_list_to_type_list(test_str))

    @hypothesis.given(strategies.lists(strategies.integers(min_value=0, max_value=len(PATHFINDER_TYPES) - 1)))
    def test_comma_separated_short_name_list_to_type_list(self, test_index_list: typing.List[int]):
        type_list = [PATHFINDER_TYPES[index][2] for index in test_index_list]
        test_str = ",".join([PATHFINDER_TYPES[index][1] for index in test_index_list])
        self.assertListEqual(type_list, AbilityManager.comma_separated_short_name_list_to_type_list(test_str))

    @hypothesis.given(
        strategies.lists(strategies.integers(min_value=0, max_value=len(PATHFINDER_TYPES) - 1)),
        strategies.lists(strategies.integers(min_value=0, max_value=len(NON_PATHFINDER_TYPES) - 1), min_size=1),
    )
    def test_comma_separated_name_list_to_type_list_non_pathfinder_type(
        self, test_index_list: typing.List[int], test_non_pathfinder_index_list: typing.List[int]
    ):
        pathfinder_examples = [PATHFINDER_TYPES[index][0] for index in test_index_list]
        for non_pathfinder in test_non_pathfinder_index_list:
            pathfinder_examples.insert(random.randint(0, len(test_index_list)), NON_PATHFINDER_TYPES[non_pathfinder][0])
        test_str = ",".join(pathfinder_examples)
        with self.assertRaises(Exception):
            AbilityManager.comma_separated_name_list_to_type_list(test_str)

    @hypothesis.given(
        strategies.lists(strategies.integers(min_value=0, max_value=len(PATHFINDER_TYPES) - 1)),
        strategies.lists(strategies.integers(min_value=0, max_value=len(NON_PATHFINDER_TYPES) - 1), min_size=1),
    )
    def test_comma_separated_short_name_list_to_type_list_non_pathfinder_type(
        self, test_index_list: typing.List[int], test_non_pathfinder_index_list: typing.List[int]
    ):
        pathfinder_examples = [PATHFINDER_TYPES[index][1] for index in test_index_list]
        for non_pathfinder in test_non_pathfinder_index_list:
            pathfinder_examples.insert(random.randint(0, len(test_index_list)), NON_PATHFINDER_TYPES[non_pathfinder][1])
        test_str = ",".join(pathfinder_examples)
        with self.assertRaises(Exception):
            AbilityManager.comma_separated_short_name_list_to_type_list(test_str)

    @hypothesis.given(strategies.integers(min_value=0))
    def test_ability_score_to_ability_modifier_always_smaller(self, score: int):
        self.assertLess(AbilityManager.ability_score_to_ability_modifier(score), score)

    def test_ability_score_to_ability_modifier_known_values(self):
        for score, modifier in ABILITY_SCORE_TO_ABILITY_MODIFIER:
            with self.subTest(f"test: score={score} modifier={modifier}"):
                self.assertEqual(AbilityManager.ability_score_to_ability_modifier(score), modifier)
