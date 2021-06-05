from typing import Set
from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock

from hypothesis import given
from hypothesis.strategies import integers, sets

from pathseeker.src.logging.logging_filter import LevelFilter


class TestLevelFilter(TestCase):
    @given(
        logging_levels_to_allow=sets(integers()),
    )
    def test_filter_true(self, logging_levels_to_allow: Set[int]):
        level_filter = LevelFilter(logging_levels_to_allow=logging_levels_to_allow)
        for level in logging_levels_to_allow:
            mock_log_record = MagicMock()
            type(mock_log_record).levelno = PropertyMock(return_value=level)

            self.assertTrue(level_filter.filter(mock_log_record))

    @given(
        logging_levels_to_allow=sets(integers()),
        different_logging_level=integers(),
    )
    def test_filter_false(self, logging_levels_to_allow: Set[int], different_logging_level: int):
        if different_logging_level not in logging_levels_to_allow:
            level_filter = LevelFilter(logging_levels_to_allow=logging_levels_to_allow)
            mock_log_record = MagicMock()

            type(mock_log_record).levelno = PropertyMock(return_value=different_logging_level)

            self.assertFalse(level_filter.filter(mock_log_record))
