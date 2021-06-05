from unittest import TestCase

from pathseeker.src.data_types.modifier_type import ModifierType
from pathseeker.src.managers.modifier_type_manager import ModifierTypeManager

PATHFINDER_TYPES = [
    ("circumstance", ModifierTypeManager.STRENGTH),
    ("item", ModifierTypeManager.DEXTERITY),
    ("status", ModifierTypeManager.CONSTITUTION),
    ("ability", ModifierTypeManager.INTELLIGENCE),
    ("proficiency", ModifierTypeManager.WISDOM),
    ("untyped", ModifierTypeManager.CHARISMA),
]

NON_PATHFINDER_TYPES = [
    ("strength", ModifierType(name="strength")),
    ("stregth", ModifierType(name="stregth")),
    ("str", ModifierType(name="str")),
    ("wis,con", ModifierType(name="wis,con")),
    ("luck", ModifierType(name="luck")),
]


class TestModifierTypeManager(TestCase):
    def test_name_to_type_pathfinder_type(self):
        for name, _, ability_score_type in PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                returned_type = ModifierTypeManager.name_to_type(name)
                self.assertEqual(returned_type, ability_score_type)

    def test_name_to_type_non_pathfinder_type(self):
        for name, _, _ in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                with self.assertRaises(Exception) as exception:
                    ModifierTypeManager.name_to_type(name)
                self.assertEqual(str(exception.exception), f'Unknown ModifierType name "{name}"')
