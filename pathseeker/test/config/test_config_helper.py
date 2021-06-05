from os import environ
from string import ascii_letters, digits
from unittest import TestCase
from unittest.mock import Mock, patch

from hypothesis import assume, example, given
from hypothesis.strategies import booleans, integers, text

from pathseeker.src.config.config_helper import TRUE_VALUES, get_environ_bool, get_environ_pos_int, get_environ_str


class TestTestConfig(TestCase):
    def setUp(self) -> None:
        self._mock_logger = Mock()

    @patch.dict(environ, {"TEST_ENV": "True"})
    def test_get_environ_bool_true(self):
        for value in TRUE_VALUES:
            self._mock_logger.reset_mock()
            with patch.dict(environ, {"TEST_ENV": value}):
                with self.subTest(value):
                    self.assertTrue(get_environ_bool(logger=self._mock_logger, environ_name="TEST_ENV"))
                    self._mock_logger.info.assert_called_once()

    @given(text(alphabet=ascii_letters + digits + " "))
    def test_get_environ_bool_false(self, value: str):
        assume(value not in TRUE_VALUES)
        self._mock_logger.reset_mock()
        with patch.dict(environ, {"TEST_ENV": value}):
            self.assertFalse(
                get_environ_bool(
                    logger=self._mock_logger,
                    environ_name="TEST_ENV",
                )
            )
            self._mock_logger.info.assert_called_once()

    def test_get_environ_bool_not_set(self):
        with patch.dict(environ, {}):
            with self.assertRaises(ValueError):
                get_environ_bool(logger=self._mock_logger, environ_name="TEST_ENV")

    @given(booleans())
    def test_get_environ_bool_not_set_default_value(self, boolean: bool):
        with patch.dict(environ, {}):
            self.assertEqual(
                get_environ_bool(logger=self._mock_logger, environ_name="TEST_ENV", default_value=boolean), boolean
            )

    @given(
        text(
            alphabet=ascii_letters + digits + " ",
        )
    )
    @example("")
    def test_get_environ_str(self, value: str):
        self._mock_logger.reset_mock()
        with patch.dict(environ, {"TEST_ENV": value}):
            self.assertEqual(
                get_environ_str(logger=self._mock_logger, environ_name="TEST_ENV", can_be_empty=True), value
            )
            self._mock_logger.info.assert_called_once()

    def test_get_environ_str_can_be_empty_false(self):
        self._mock_logger.reset_mock()
        with patch.dict(environ, {"TEST_ENV": ""}):
            with self.assertRaises(ValueError):
                get_environ_str(logger=self._mock_logger, environ_name="TEST_ENV")

    @given(text(alphabet=ascii_letters + digits + " "))
    def test_get_environ_str_not_set(self, value: str):
        with patch.dict(environ, {}):
            self.assertEqual(
                get_environ_str(
                    logger=self._mock_logger, environ_name="TEST_ENV", can_be_empty=True, default_value=value
                ),
                value,
            )

    def test_get_environ_str_not_set_default_value(self):
        with patch.dict(environ, {}):
            with self.assertRaises(ValueError):
                get_environ_str(logger=self._mock_logger, environ_name="TEST_ENV")

    @given(integers(min_value=0))
    def test_get_environ_int(self, value: int):
        self._mock_logger.reset_mock()
        with patch.dict(environ, {"TEST_ENV": str(value)}):
            self.assertEqual(get_environ_pos_int(logger=self._mock_logger, environ_name="TEST_ENV"), value)
            self._mock_logger.info.assert_called_once()

    @given(
        text(
            alphabet=ascii_letters + " ",
        )
    )
    @example("")
    def test_get_environ_non_int(self, value: str):
        self._mock_logger.reset_mock()
        with patch.dict(environ, {"TEST_ENV": value}):
            with self.assertRaises(ValueError):
                get_environ_pos_int(logger=self._mock_logger, environ_name="TEST_ENV")

    @given(integers(min_value=0))
    def test_get_environ_int_not_set(self, value: int):
        with patch.dict(environ, {}):
            self.assertEqual(
                get_environ_pos_int(logger=self._mock_logger, environ_name="TEST_ENV", default_value=value), value
            )

    def test_get_environ_int_not_set_default_value(self):
        with patch.dict(environ, {}):
            with self.assertRaises(ValueError):
                get_environ_pos_int(logger=self._mock_logger, environ_name="TEST_ENV")
