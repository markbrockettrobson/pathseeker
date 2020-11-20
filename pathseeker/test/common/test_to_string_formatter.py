import string
import typing
import unittest

import hypothesis
import hypothesis.strategies as strategies

import pathseeker.src.common.to_string_formatter as to_string_formatter


class TestToStringFormatter(unittest.TestCase):
    @hypothesis.given(
        class_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        value=strategies.text(alphabet=string.ascii_letters, min_size=1),
    )
    def test_to_string_one_prams(self, class_name: str, name: str, value: str):
        self.assertEqual(
            f"{class_name}: {name}={value}",
            to_string_formatter.ToStringFormatter.to_string(
                class_name, **{name: value}
            ),
        )

    @hypothesis.given(
        class_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        name_list=strategies.lists(
            strategies.text(alphabet=string.ascii_letters, min_size=1),
            min_size=2,
            max_size=2,
            unique=True,
        ),
        value_list=strategies.lists(
            strategies.text(alphabet=string.ascii_letters, min_size=1),
            min_size=2,
            max_size=2,
        ),
    )
    def test_to_string_two_prams(
        self, class_name: str, name_list: typing.List[str], value_list: typing.List[str]
    ):
        self.assertEqual(
            f"{class_name}: {name_list[0]}={value_list[0]}, {name_list[1]}={value_list[1]}",
            to_string_formatter.ToStringFormatter.to_string(
                class_name,
                **{name_list[index]: value_list[index] for index in range(2)},
            ),
        )
