from typing import List, Union
from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock

from hypothesis import given
from hypothesis.strategies import floats, integers, lists, one_of, text

from pathseeker.interface.modifier.i_modifiable_brakedown import IModifiableBrakedown
from pathseeker.src.modifier.modifiable_brakedown import ModifiableBrakedown


class TestModifiableBrakedown(TestCase):
    def setUp(self) -> None:
        self._mock_int_brakedowns = [MagicMock(IModifiableBrakedown) for _ in range(4)]
        for index, mock_brakedown in enumerate(self._mock_int_brakedowns):
            mock_brakedown.get_simple_string.return_value = (
                f"    {index} mock_brakedown_name_{index}\n\t1 subbrakedown_part1"
            )
            mock_brakedown.get_detailed_string.return_value = (
                f"    {index} mock_brakedown_name_{index}\n\t1 subbrakedown_part1\n\t\t1 subbrakedown_part2"
            )
            type(mock_brakedown).value = PropertyMock(return_value=index)
            type(mock_brakedown).name = PropertyMock(return_value=f"mock_brakedown_name_{index}")
            type(mock_brakedown).priority = PropertyMock(return_value=index)

    @given(value=one_of([integers(), floats(allow_nan=False), text()]))
    def test_value(self, value: Union[int, float, str]):
        test_brakedown = ModifiableBrakedown(name="test_name", value=value)

        self.assertEqual(test_brakedown.value, value)

    @given(name=text())
    def test_name(self, name: str):
        test_brakedown = ModifiableBrakedown(name=name, value=0)

        self.assertEqual(test_brakedown.name, name)

    @given(priority=integers())
    def test_priority(self, priority: int):
        test_brakedown = ModifiableBrakedown(name="test_name", value=0, priority=priority)

        self.assertEqual(test_brakedown.priority, priority)

    def test_get_simple_string_simple(self):
        test_brakedown = ModifiableBrakedown(name="test_name", value=0)

        self.assertEqual(test_brakedown.get_simple_string(), "   0 test_name")

    def test_get_detailed_string_simple(self):
        test_brakedown = ModifiableBrakedown(name="test_name", value=0)

        self.assertEqual(test_brakedown.get_detailed_string(), "   0 test_name")

    @given(modifiable_brakedown_indexes=lists(integers(min_value=0, max_value=3), unique=True, min_size=1, max_size=4))
    def test_get_simple_string(self, modifiable_brakedown_indexes: List[int]):
        modifiable_brakedown_indexes.sort()
        modifiable_brakedowns = [self._mock_int_brakedowns[index] for index in modifiable_brakedown_indexes]
        test_brakedown = ModifiableBrakedown(name="test_name", value=0, modifiable_brakedowns=modifiable_brakedowns)

        expected_string = "   0 test_name"
        for modifiable_brakedown in modifiable_brakedowns:
            expected_string += "\n\t%4s %s" % (modifiable_brakedown.value, modifiable_brakedown.name)

        self.assertEqual(test_brakedown.get_simple_string(), expected_string)

    @given(modifiable_brakedown_indexes=lists(integers(min_value=0, max_value=3), unique=True, min_size=1, max_size=4))
    def test_get_detailed_string(self, modifiable_brakedown_indexes: List[int]):
        modifiable_brakedown_indexes.sort()
        modifiable_brakedowns = [self._mock_int_brakedowns[index] for index in modifiable_brakedown_indexes]
        test_brakedown = ModifiableBrakedown(name="test_name", value=0, modifiable_brakedowns=modifiable_brakedowns)

        expected_string = "   0 test_name"
        for modifiable_brakedown in modifiable_brakedowns:
            expected_string += f"\n\t    {modifiable_brakedown.value} mock_brakedown_name_{modifiable_brakedown.value}\n\t\t\t1 subbrakedown_part1\n\t\t\t\t1 subbrakedown_part2"

        self.assertEqual(test_brakedown.get_detailed_string(), expected_string)
