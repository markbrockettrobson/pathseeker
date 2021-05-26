from unittest import TestCase

from hypothesis import given
from hypothesis.strategies import integers

from pathseeker.src.data_types.ability import Ability
from pathseeker.src.managers.ability_manager import AbilityManager

PATHFINDER_TYPES = [
    ("strength", "STR", AbilityManager.STRENGTH),
    ("dexterity", "DEX", AbilityManager.DEXTERITY),
    ("constitution", "CON", AbilityManager.CONSTITUTION),
    ("intelligence", "INT", AbilityManager.INTELLIGENCE),
    ("wisdom", "WIS", AbilityManager.WISDOM),
    ("charisma", "CHA", AbilityManager.CHARISMA),
]

NON_PATHFINDER_TYPES = [
    ("stregth", "STRENGTH", Ability(name="stregth", short_name="STRENGTH")),
    ("str", "STRENGTH", Ability(name="str", short_name="STRENGTH")),
    ("wis,con", "DAX", Ability(name="wis,con", short_name="DAX")),
    ("luck", "LUK", Ability(name="luck", short_name="LUK")),
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


class TestAbilityManager(TestCase):
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

    @given(integers(min_value=-10))
    def test_ability_score_to_ability_modifier_smaller(self, score: int):
        self.assertLessEqual(AbilityManager.ability_score_to_ability_modifier(score), score)

    @given(integers(max_value=-10))
    def test_ability_score_to_ability_modifier_larger(self, score: int):
        self.assertGreaterEqual(AbilityManager.ability_score_to_ability_modifier(score), score)

    def test_ability_score_to_ability_modifier_known_values(self):
        for score, modifier in ABILITY_SCORE_TO_ABILITY_MODIFIER:
            with self.subTest(f"test: score={score} modifier={modifier}"):
                self.assertEqual(AbilityManager.ability_score_to_ability_modifier(score), modifier)
