from unittest import TestCase

from pathseeker.src.managers.modifier_type_manager import ModifierTypeManager

PATHFINDER_TYPES = [
    ("ability", ModifierTypeManager.ABILITY, ModifierTypeManager.HIGHEST_ONLY),
    ("base", ModifierTypeManager.BASE, ModifierTypeManager.HIGHEST_ONLY),
    ("circumstance", ModifierTypeManager.CIRCUMSTANCE, ModifierTypeManager.HIGHEST_ONLY),
    ("item", ModifierTypeManager.ITEM, ModifierTypeManager.HIGHEST_ONLY),
    ("proficiency", ModifierTypeManager.PROFICIENCY, ModifierTypeManager.HIGHEST_ONLY),
    ("status", ModifierTypeManager.STATUS, ModifierTypeManager.HIGHEST_ONLY),
    ("untyped", ModifierTypeManager.UNTYPED, ModifierTypeManager.STACKS),
]

NON_PATHFINDER_TYPES = [
    "strength",
    "stregth",
    "str",
    "wis,con",
    "luck",
]


class TestModifierTypeManager(TestCase):
    def test_name_to_type_pathfinder_type(self):
        for name, modifier_type, _ in PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                returned_type = ModifierTypeManager.name_to_type(name)
                self.assertEqual(returned_type, modifier_type)

    def test_name_to_type_non_pathfinder_type(self):
        for name in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                with self.assertRaises(Exception) as exception:
                    ModifierTypeManager.name_to_type(name)
                self.assertEqual(str(exception.exception), f'Unknown ModifierType name "{name}"')

    def test_name_to_duplicate_modifier_type_manager_true(self):
        for name, _, duplicate_rule in PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                returned_type = ModifierTypeManager.name_to_duplicate_rule(name)
                self.assertEqual(returned_type, duplicate_rule)

    def test_name_to_duplicate_modifier_type_manager_unknown(self):
        for name in NON_PATHFINDER_TYPES:
            with self.subTest(f"test: name={name}"):
                with self.assertRaises(Exception) as exception:
                    ModifierTypeManager.name_to_duplicate_rule(name)
                    self.assertEqual(str(exception.exception), f'Unknown ModifierType name "{name}"')
