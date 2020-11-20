import string
import unittest

import hypothesis
import hypothesis.strategies as strategies

import pathseeker.src.data_types.size as size


class TestSize(unittest.TestCase):
    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        space=strategies.integers(),
        tall_reach=strategies.integers(),
        long_reach=strategies.integers(),
    )
    def test_get_name(
        self, name: str, short_name: str, space: int, tall_reach: int, long_reach: int
    ):
        test_size = size.Size(
            name=name,
            short_name=short_name,
            space=space,
            tall_reach=tall_reach,
            long_reach=long_reach,
        )
        self.assertEqual(test_size.name, name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        space=strategies.integers(),
        tall_reach=strategies.integers(),
        long_reach=strategies.integers(),
    )
    def test_get_short_name(
        self, name: str, short_name: str, space: int, tall_reach: int, long_reach: int
    ):
        test_size = size.Size(
            name=name,
            short_name=short_name,
            space=space,
            tall_reach=tall_reach,
            long_reach=long_reach,
        )
        self.assertEqual(test_size.short_name, short_name)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        space=strategies.integers(),
        tall_reach=strategies.integers(),
        long_reach=strategies.integers(),
    )
    def test_get_space(
        self, name: str, short_name: str, space: int, tall_reach: int, long_reach: int
    ):
        test_size = size.Size(
            name=name,
            short_name=short_name,
            space=space,
            tall_reach=tall_reach,
            long_reach=long_reach,
        )
        self.assertEqual(test_size.space, space)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        space=strategies.integers(),
        tall_reach=strategies.integers(),
        long_reach=strategies.integers(),
    )
    def test_get_tall_reach(
        self, name: str, short_name: str, space: int, tall_reach: int, long_reach: int
    ):
        test_size = size.Size(
            name=name,
            short_name=short_name,
            space=space,
            tall_reach=tall_reach,
            long_reach=long_reach,
        )
        self.assertEqual(test_size.tall_reach, tall_reach)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        space=strategies.integers(),
        tall_reach=strategies.integers(),
        long_reach=strategies.integers(),
    )
    def test_get_long_reach(
        self, name: str, short_name: str, space: int, tall_reach: int, long_reach: int
    ):
        test_size = size.Size(
            name=name,
            short_name=short_name,
            space=space,
            tall_reach=tall_reach,
            long_reach=long_reach,
        )
        self.assertEqual(test_size.long_reach, long_reach)

    @hypothesis.given(
        name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        short_name=strategies.text(alphabet=string.ascii_letters, min_size=1),
        space=strategies.integers(),
        tall_reach=strategies.integers(),
        long_reach=strategies.integers(),
    )
    def test_str(
        self, name: str, short_name: str, space: int, tall_reach: int, long_reach: int
    ):
        test_size = size.Size(
            name=name,
            short_name=short_name,
            space=space,
            tall_reach=tall_reach,
            long_reach=long_reach,
        )
        self.assertEqual(
            str(test_size),
            f"Size: name={name},"
            f" short_name={short_name},"
            f" space={space},"
            f" tall_reach={tall_reach},"
            f" long_reach={long_reach}",
        )
