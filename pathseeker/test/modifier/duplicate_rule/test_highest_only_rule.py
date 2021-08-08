from typing import List
from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock

from hypothesis import given
from hypothesis.strategies import integers, lists

from pathseeker.interface.modifier.i_modifier import IModifier
from pathseeker.src.modifier.duplicate_rule.highest_only_rule import HighestOnly


class TestHighestOnly(TestCase):
    def setUp(self) -> None:
        self._mock_modifiers = [MagicMock(IModifier[int]) for _ in range(10)]
        for index, mock_modifier in enumerate(self._mock_modifiers):
            type(mock_modifier).value = PropertyMock(return_value=index)

    @given(lists(integers(min_value=0, max_value=9), min_size=1, max_size=10))
    def test_apply_rule(self, collection_indexes: List[int]):
        collection = list(map(self._mock_modifiers.__getitem__, collection_indexes))
        output_collection = HighestOnly.apply_rule(collection)
        self.assertSetEqual({self._mock_modifiers[max(collection_indexes)]}, set(output_collection))

    def test_apply_rule_empty_set(self):
        output_collection = HighestOnly.apply_rule([])
        self.assertSetEqual(set(), set(output_collection))
