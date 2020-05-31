import string
import unittest

import hypothesis
import hypothesis.strategies as strategies

import pathseeker.src.proficiency_rank as proficiency_rank


class TestProficiencyRank(unittest.TestCase):
    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        value=strategies.integers(),
    )
    def test_get_name(self, name: str, short_name: str, value: int):
        test_proficiency_rank = proficiency_rank.ProficiencyRank(
            name=name, short_name=short_name, value=value
        )
        self.assertEqual(test_proficiency_rank.name, name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        value=strategies.integers(),
    )
    def test_get_short_name(self, name: str, short_name: str, value: int):
        test_proficiency_rank = proficiency_rank.ProficiencyRank(
            name=name, short_name=short_name, value=value
        )
        self.assertEqual(test_proficiency_rank.short_name, short_name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        value=strategies.integers(),
    )
    def test_get_space(self, name: str, short_name: str, value: int):
        test_proficiency_rank = proficiency_rank.ProficiencyRank(
            name=name, short_name=short_name, value=value
        )
        self.assertEqual(test_proficiency_rank.value, value)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        value=strategies.integers(),
    )
    def test_str(self, name: str, short_name: str, value: int):
        test_proficiency_rank = proficiency_rank.ProficiencyRank(
            name=name, short_name=short_name, value=value
        )
        self.assertEqual(
            str(test_proficiency_rank),
            f"ProficiencyRank: name={name},"
            f" short_name={short_name},"
            f" value={value}",
        )
