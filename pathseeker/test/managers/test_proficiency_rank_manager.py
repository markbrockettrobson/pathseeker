import unittest
import unittest.mock as mock

from pathseeker.interface.data_types.i_proficiency_rank import IProficiencyRank
from pathseeker.src.managers.proficiency_rank_manager import ProficiencyRankManager

PATHFINDER_TYPES = [
    ("untrained", "U", ProficiencyRankManager.UNTRAINED),
    ("trained", "T", ProficiencyRankManager.TRAINED),
    ("expert", "E", ProficiencyRankManager.EXPERT),
    ("master", "M", ProficiencyRankManager.MASTER),
    ("legendary", "L", ProficiencyRankManager.LEGENDARY),
]

NON_PATHFINDER_TYPES = [
    ("stregth", "STR", mock.create_autospec(IProficiencyRank)),
    ("1", "2", mock.create_autospec(IProficiencyRank)),
    ("Legendary", "dexterity", mock.create_autospec(IProficiencyRank)),
    ("EXPERT", "e", mock.create_autospec(IProficiencyRank)),
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
