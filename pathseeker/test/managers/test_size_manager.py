from unittest import TestCase

from pathseeker.src.data_types.size import Size
from pathseeker.src.managers.size_manager import SizeManager

PATHFINDER_SIZES = [
    ("tiny", "T", SizeManager.TINY),
    ("small", "S", SizeManager.SMALL),
    ("medium", "M", SizeManager.MEDIUM),
    ("large", "L", SizeManager.LARGE),
    ("huge", "H", SizeManager.HUGE),
    ("gargantuan", "G", SizeManager.GARGANTUAN),
]

NON_PATHFINDER_SIZES = [
    ("big", "B"),
    ("very_big", "VERY_BIG"),
    ("smallish", "SY"),
    ("constitution", "CON"),
]


class TestSizeManager(TestCase):
    def test_name_to_size_pathfinder_size(self):
        for name, _, size in PATHFINDER_SIZES:
            with self.subTest(f"test: name={name}"):
                returned_size = SizeManager.name_to_size(name)
                self.assertEqual(returned_size, size)

    def test_short_name_to_type_pathfinder_size(self):
        for _, short_name, size in PATHFINDER_SIZES:
            with self.subTest(f"test: short_name={short_name}"):
                returned_size = SizeManager.short_name_to_size(short_name)
                self.assertEqual(returned_size, size)

    def test_name_to_type_non_pathfinder_type(self):
        for name, _ in NON_PATHFINDER_SIZES:
            with self.subTest(f"test: name={name}"):
                with self.assertRaises(Exception) as exception:
                    SizeManager.name_to_size(name)
                self.assertEqual(str(exception.exception), f'Unknown Size name "{name}"')

    def test_short_name_to_type_non_pathfinder_type(self):
        for _, short_name in NON_PATHFINDER_SIZES:
            with self.subTest(f"test: short_name={short_name}"):
                with self.assertRaises(Exception) as exception:
                    SizeManager.short_name_to_size(short_name)
                self.assertEqual(str(exception.exception), f'Unknown Size short name "{short_name}"')
