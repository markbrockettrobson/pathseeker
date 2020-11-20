import unittest
import unittest.mock as mock

import pathseeker.interface.data_types.i_proficiency_rank as i_proficiency_rank
import pathseeker.src.managers.proficiency_rank_manager as proficiency_rank_manager

PATHFINDER_TYPES = [
    ("untrained", "U", proficiency_rank_manager.ProficiencyRankManager.UNTRAINED),
    ("trained", "T", proficiency_rank_manager.ProficiencyRankManager.TRAINED),
    ("expert", "E", proficiency_rank_manager.ProficiencyRankManager.EXPERT),
    ("master", "M", proficiency_rank_manager.ProficiencyRankManager.MASTER),
    ("legendary", "L", proficiency_rank_manager.ProficiencyRankManager.LEGENDARY),
]

NON_PATHFINDER_TYPES = [
    ("stregth", "STR", mock.create_autospec(i_proficiency_rank.IProficiencyRank)),
    ("1", "2", mock.create_autospec(i_proficiency_rank.IProficiencyRank)),
    (
        "Legendary",
        "dexterity",
        mock.create_autospec(i_proficiency_rank.IProficiencyRank),
    ),
    ("EXPERT", "e", mock.create_autospec(i_proficiency_rank.IProficiencyRank)),
]


class TestAbilityManager(unittest.TestCase):
    def test_name_to_type_pathfinder_type(self):
        for name, _, ability_score_type in PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                returned_type = proficiency_rank_manager.ProficiencyRankManager.name_to_type(
                    name
                )
                self.assertEqual(returned_type, ability_score_type)

    def test_short_name_to_type_pathfinder_type(self):
        for _, short_name, ability_score_type in PATHFINDER_TYPES:
            with self.subTest(f"test: short_name={short_name}"):
                returned_type = proficiency_rank_manager.ProficiencyRankManager.short_name_to_type(
                    short_name
                )
                self.assertEqual(returned_type, ability_score_type)

    def test_name_to_type_non_pathfinder_type(self):
        for name, _, _ in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                with self.assertRaises(Exception) as exception:
                    proficiency_rank_manager.ProficiencyRankManager.name_to_type(name)
                self.assertEqual(
                    str(exception.exception), f'Unknown proficiency rank name "{name}"'
                )

    def test_short_name_to_type_non_pathfinder_type(self):
        for _, short_name, _ in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: short_name={short_name}"):
                with self.assertRaises(Exception) as exception:
                    proficiency_rank_manager.ProficiencyRankManager.short_name_to_type(
                        short_name
                    )
                self.assertEqual(
                    str(exception.exception),
                    f'Unknown proficiency rank short name "{short_name}"',
                )
