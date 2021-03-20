import unittest

import hypothesis
import hypothesis.strategies as strategies

from pathseeker.src.data_types.ability import Ability
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
    ("stregth", "STRENGTH", Ability(name="stregth", short_name="STRENGTH")),
    ("1", "2", Ability(name="1", short_name="2")),
    ("WIS,CON", "dexterity", Ability(name="WIS,CON", short_name="dexterity")),
    ("CONSTITUTION", "con", Ability(name="CONSTITUTION", short_name="con")),
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

    @hypothesis.given(strategies.integers(min_value=0))
    def test_ability_score_to_ability_modifier_always_smaller(self, score: int):
        self.assertLess(AbilityManager.ability_score_to_ability_modifier(score), score)

    def test_ability_score_to_ability_modifier_known_values(self):
        for score, modifier in ABILITY_SCORE_TO_ABILITY_MODIFIER:
            with self.subTest(f"test: score={score} modifier={modifier}"):
                self.assertEqual(AbilityManager.ability_score_to_ability_modifier(score), modifier)
