import unittest
import unittest.mock as mock

import pathseeker.interface.i_size as i_size
import pathseeker.src.size_manager as size_manager

PATHFINDER_SIZES = [
    ("tiny", "T", size_manager.SizeManager.TINY),
    ("small", "S", size_manager.SizeManager.SMALL),
    ("medium", "M", size_manager.SizeManager.MEDIUM),
    ("large", "L", size_manager.SizeManager.LARGE),
    ("huge", "H", size_manager.SizeManager.HUGE),
    ("gargantuan", "G", size_manager.SizeManager.GARGANTUAN),
]

NON_PATHFINDER_SIZES = [
    ("big", "B", mock.create_autospec(i_size.ISize)),
    ("1", "2", mock.create_autospec(i_size.ISize)),
    ("SMall", "s", mock.create_autospec(i_size.ISize)),
    ("CONSTITUTION", "con", mock.create_autospec(i_size.ISize)),
]


class TestSizeManager(unittest.TestCase):
    def test_name_to_size_pathfinder_size(self):
        for name, _, size in PATHFINDER_SIZES:
            with self.subTest(f"test: name={name}"):
                returned_size = size_manager.SizeManager.name_to_size(name)
                self.assertEqual(returned_size, size)

    def test_short_name_to_type_pathfinder_size(self):
        for _, short_name, size in PATHFINDER_SIZES:
            with self.subTest(f"test: short_name={short_name}"):
                returned_size = size_manager.SizeManager.short_name_to_size(short_name)
                self.assertEqual(returned_size, size)

    def test_name_to_type_non_pathfinder_type(self):
        for name, _, _ in NON_PATHFINDER_SIZES:
            with self.subTest(f"test: name={name}"):
                with self.assertRaises(Exception) as exception:
                    size_manager.SizeManager.name_to_size(name)
                self.assertEqual(
                    str(exception.exception), f'Unknown size name "{name}"'
                )

    def test_short_name_to_type_non_pathfinder_type(self):
        for _, short_name, _ in NON_PATHFINDER_SIZES:
            with self.subTest(f"test: short_name={short_name}"):
                with self.assertRaises(Exception) as exception:
                    size_manager.SizeManager.short_name_to_size(short_name)
                self.assertEqual(
                    str(exception.exception), f'Unknown size short name "{short_name}"'
                )
