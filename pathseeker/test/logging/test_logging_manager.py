from logging import INFO, getLogger
from unittest import TestCase

from pathseeker.src.logging.logging_manager import LoggingManager


class TestLoggingManager(TestCase):
    def test_logger_sets_level(self):
        LoggingManager.get_logger(__name__)
        self.assertEqual(getLogger("pathseeker").level, INFO)

    def test_logger_adds_handlers_once_only(self):
        starting_handler_count = len(getLogger().handlers)
        for name in ["a", "b", "c", "a.b", "a.b.c"]:
            LoggingManager.get_logger(name)
            self.assertEqual(len(getLogger().handlers), starting_handler_count)

    def test_logger_name(self):
        for name in ["a", "b", "c", "a.b", "a.b.c"]:
            self.assertEqual(LoggingManager.get_logger(name).name, f"pathseeker.{name}")

    def test_child_logger_name(self):
        parent_logger = getLogger("test.start")
        for name in ["a", "b", "c", "a.b", "a.b.c"]:
            self.assertEqual(
                LoggingManager.get_child_logger(name, parent_logger=parent_logger).name, f"test.start.{name}"
            )

    def test_child_logger_name_no_parent(self):
        for name in ["a", "b", "c", "a.b", "a.b.c"]:
            self.assertEqual(LoggingManager.get_child_logger(name).name, f"pathseeker.{name}")

    def test_child_logger_name_empty(self):
        with self.assertRaises(ValueError):
            LoggingManager.get_child_logger("")
