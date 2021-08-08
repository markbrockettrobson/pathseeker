from typing import Union
from unittest import TestCase
from unittest.mock import MagicMock

from hypothesis import given
from hypothesis.strategies import floats, integers, one_of, text

from pathseeker.src.data_types.modifier_type import ModifierType
from pathseeker.src.modifier.add_modifier import AddModifier


class TestAddModifier(TestCase):
    def setUp(self) -> None:
        self._mock_modifier_type = MagicMock(ModifierType)

    def test_modifier_type(self):
        test_modifier = AddModifier(name="name", value=1, modifier_type=self._mock_modifier_type, priority=1)
        self.assertEqual(test_modifier.modifier_type, self._mock_modifier_type)

    @given(name=text())
    def test_name(self, name: str):
        test_modifier = AddModifier(name=name, value=1, modifier_type=self._mock_modifier_type, priority=1)
        self.assertEqual(test_modifier.name, name)

    @given(priority=integers())
    def test_priority(self, priority: int):
        test_modifier = AddModifier(name="name", value=1, modifier_type=self._mock_modifier_type, priority=priority)
        self.assertEqual(test_modifier.priority, priority)

    @given(value=one_of(integers(), floats(allow_nan=False, allow_infinity=False)))
    def test_value(self, value: Union[int, float]):
        test_modifier = AddModifier(name="name", value=value, modifier_type=self._mock_modifier_type, priority=1)
        self.assertEqual(test_modifier.value, value)

    @given(value=integers(), base_value=integers())
    def test_modify_value_int(self, value: int, base_value: int):
        test_modifier = AddModifier(name="name", value=value, modifier_type=self._mock_modifier_type, priority=1)
        self.assertEqual(test_modifier.modify_value(base_value), base_value + value)

    @given(
        value=floats(allow_nan=False, allow_infinity=False), base_value=floats(allow_nan=False, allow_infinity=False)
    )
    def test_modify_value_float(self, value: int, base_value: int):
        test_modifier = AddModifier(name="name", value=value, modifier_type=self._mock_modifier_type, priority=1)
        self.assertEqual(test_modifier.modify_value(base_value), base_value + value)
