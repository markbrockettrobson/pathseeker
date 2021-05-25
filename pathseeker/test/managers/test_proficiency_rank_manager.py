import unittest

from pathseeker.src.data_types.proficiency_rank import ProficiencyRank
from pathseeker.src.managers.proficiency_rank_manager import ProficiencyRankManager

PATHFINDER_TYPES = [
    ("untrained", "U", ProficiencyRankManager.UNTRAINED),
    ("trained", "T", ProficiencyRankManager.TRAINED),
    ("expert", "E", ProficiencyRankManager.EXPERT),
    ("master", "M", ProficiencyRankManager.MASTER),
    ("legendary", "L", ProficiencyRankManager.LEGENDARY),
]

NON_PATHFINDER_TYPES = [
    ("stregth", "STR", ProficiencyRank(name="stregth", short_name="STR", value=2, add_level=True)),
    ("dex", "DEXTERITY", ProficiencyRank(name="dex", short_name="DEXTERITY", value=4, add_level=True)),
    ("dexterity", "DEX", ProficiencyRank(name="dexterity", short_name="DEX", value=6, add_level=True)),
    ("experts", "EEEE", ProficiencyRank(name="experts", short_name="EEEE", value=8, add_level=True)),
]


class TestAbilityManager(unittest.TestCase):
    def test_name_to_type_pathfinder_type(self):
        for name, _, ability_score_type in PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                returned_type = ProficiencyRankManager.name_to_type(name)
                self.assertEqual(returned_type, ability_score_type)

    def test_short_name_to_type_pathfinder_type(self):
        for _, short_name, ability_score_type in PATHFINDER_TYPES:
            with self.subTest(f"test: short_name={short_name}"):
                returned_type = ProficiencyRankManager.short_name_to_type(short_name)
                self.assertEqual(returned_type, ability_score_type)

    def test_name_to_type_non_pathfinder_type(self):
        for name, _, _ in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                with self.assertRaises(Exception) as exception:
                    ProficiencyRankManager.name_to_type(name)
                self.assertEqual(str(exception.exception), f'Unknown ProficiencyRank name "{name}"')

    def test_short_name_to_type_non_pathfinder_type(self):
        for _, short_name, _ in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: short_name={short_name}"):
                with self.assertRaises(Exception) as exception:
                    ProficiencyRankManager.short_name_to_type(short_name)
                self.assertEqual(str(exception.exception), f'Unknown ProficiencyRank short name "{short_name}"')
