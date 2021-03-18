import unittest
import unittest.mock as mock

from pathseeker.interface.data_types.i_modifier_type import IModifierType
from pathseeker.src.managers.modifier_type_manager import ModifierTypeManager

PATHFINDER_TYPES = [
    ("circumstance", "C", ModifierTypeManager.CIRCUMSTANCE),
    ("item", "I", ModifierTypeManager.ITEM),
    ("proficiency", "P", ModifierTypeManager.PROFICIENCY),
    ("status", "S", ModifierTypeManager.STATUS),
    ("untyped", "U", ModifierTypeManager.UNTYPED),
]

NON_PATHFINDER_TYPES = [
    ("stregth", "STR", mock.create_autospec(IModifierType)),
    ("1", "2", mock.create_autospec(IModifierType)),
    ("Legendary", "dexterity", mock.create_autospec(IModifierType)),
    ("EXPERT", "e", mock.create_autospec(IModifierType)),
    ("Circumstance", "c", mock.create_autospec(IModifierType)),
    ("Item", "i", mock.create_autospec(IModifierType)),
]


class TestModifierTypeManager(unittest.TestCase):
    def test_name_to_type_pathfinder_type(self):
        for name, _, modifier_type in PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                returned_type = ModifierTypeManager.name_to_type(name)
                self.assertEqual(returned_type, modifier_type)

    def test_short_name_to_type_pathfinder_type(self):
        for _, short_name, modifier_type in PATHFINDER_TYPES:
            with self.subTest(f"test: short_name={short_name}"):
                returned_type = ModifierTypeManager.short_name_to_type(short_name)
                self.assertEqual(returned_type, modifier_type)

    def test_name_to_type_non_pathfinder_type(self):
        for name, _, _ in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                with self.assertRaises(Exception) as exception:
                    ModifierTypeManager.name_to_type(name)
                self.assertEqual(str(exception.exception), f'Unknown ModifierType name "{name}"')

    def test_short_name_to_type_non_pathfinder_type(self):
        for _, short_name, _ in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: short_name={short_name}"):
                with self.assertRaises(Exception) as exception:
                    ModifierTypeManager.short_name_to_type(short_name)
                self.assertEqual(str(exception.exception), f'Unknown ModifierType short name "{short_name}"')
