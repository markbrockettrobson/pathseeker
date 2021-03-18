import unittest
import unittest.mock as mock
import typing
import json

import hypothesis
import hypothesis.strategies as strategies

from pathseeker.interface.common.i_data_type import IDataType
from pathseeker.src.common.data_type_base import DataTypeBase


class TestDataType:

    INTERFACE_TO_TEST = IDataType
    CLASS_TO_TEST = DataTypeBase

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_to_json_dict(self, test_data_type: IDataType):
        raise NotImplemented()

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_validate_dict(self, test_data_type: IDataType):
        self.assertTrue(TestDataType.CLASS_TO_TEST.validate_json(test_data_type.to_json_dict()))

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_build_from_dict(self, test_data_type: IDataType):
        recreated_test_data_type = TestDataType.CLASS_TO_TEST.build_from_json_dict(test_data_type.to_json_dict())

        self.assertEqual(recreated_test_data_type, test_data_type)

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_to_json_string_implemented(self, test_data_type: IDataType):
        json_string = test_data_type.to_json_string()
        json_dict = json.loads(json_string)
        recreated_test_data_type = TestDataType.CLASS_TO_TEST.build_from_json_dict(json_dict)

        self.assertEqual(recreated_test_data_type, test_data_type)

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_to_json_string(self, test_data_type: IDataType):
        raise NotImplemented()

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_to_string_implemented(self, test_data_type: IDataType):
        _ = str(test_data_type)

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_equal_same_object(self, test_data_type: IDataType):
        self.assertTrue(test_data_type == test_data_type)

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_types=strategies.lists(CLASS_TO_TEST.strategy(), min_size=2, max_size=2, unique=True))
    def test_equal_different_objects(self, test_data_types: typing.List[IDataType]):
        self.assertFalse(test_data_types[0] == test_data_types[1])

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_equal_different_object_types(self, test_data_type: IDataType):
        test_objects = {
            "string": "string",
            "int": 1,
            "float": 2.2,
            "list": ["a", "list"],
            "set": {"a", "set"},
            "dict": {"a": "json", "dictionary": "flat"},
            "data_type": mock.create_autospec(IDataType),
        }
        for test_name, test_object in test_objects.items():
            with self.subTest(f"test: name={test_name}"):
                self.assertFalse(test_data_type == test_object)

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_equal_same_object(self, test_data_type: IDataType):
        self.assertTrue(test_data_type == test_data_type)

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_hash_same_object(self, test_data_type: IDataType):
        self.assertEqual(hash(test_data_type), hash(test_data_type))

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_types=strategies.lists(CLASS_TO_TEST.strategy(), min_size=2, max_size=2, unique=True))
    def test_hash_recreated_object(self, test_data_types: typing.List[IDataType]):
        self.assertNotEqual(hash(test_data_types[0]), hash(test_data_types[1]))

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_hash_different_objects(self, test_data_type: IDataType):
        test_objects = {
            "string": "string",
            "int": 1,
            "float": 2.2,
            "list": ["a", "list"],
            "set": {"a", "set"},
            "dict": {"a": "json", "dictionary": "flat"},
            "data_type": mock.create_autospec(IDataType),
        }
        for test_name, test_object in test_objects.items():
            with self.subTest(f"test: name={test_name}"):
                self.assertNotEqual(hash(test_data_type), hash(test_object))

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_copy(self, test_data_type: IDataType):
        self.assertEqual(str(test_data_type.__copy__()), str(test_data_type))

    # @unittest.skipIf(__name__ == "test_data_type_base", "base tests")
    @hypothesis.given(test_data_type=CLASS_TO_TEST.strategy())
    def test_deep_copy(self, test_data_type: IDataType):
        self.assertEqual(hash(test_data_type.__deepcopy__()), hash(test_data_type))
