from unittest import TestCase, skipIf

from pathseeker.src.config.test_config import RUN_SQL_INTEGRATION_TEST
from pathseeker.src.database.tables.trait import Trait
from pathseeker.src.flask_app.app_factory import DATABASE


class TestTrait(TestCase):
    def setUp(self) -> None:
        names = ["1", "2", "3", "4", "5"]
        types = [None, "even", None, "even", None]
        self._in_db_traits = [Trait(name=name, type=types[index]) for index, name in enumerate(names)]

        for trait in self._in_db_traits:
            DATABASE.session.add(trait)
        DATABASE.session.commit()

    def tearDown(self) -> None:
        for trait in self._in_db_traits:
            DATABASE.session.delete(trait)
        DATABASE.session.commit()

    @skipIf(not RUN_SQL_INTEGRATION_TEST, "Sql db needed for test")
    def test_can_find_all_trait(self):
        for trait in self._in_db_traits:
            with self.subTest(trait.name):
                self.assertEqual(Trait.query.filter_by(name=trait.name).first(), trait)

    @skipIf(not RUN_SQL_INTEGRATION_TEST, "Sql db needed for test")
    def test_trait_str(self):
        for trait in self._in_db_traits:
            with self.subTest(trait.name):
                print(trait, trait.name)
                self.assertEqual(f"<Trait {trait.name}>", str(trait))

    @skipIf(not RUN_SQL_INTEGRATION_TEST, "Sql db needed for test")
    def test_trait_repr(self):
        for trait in self._in_db_traits:
            with self.subTest(trait.name):
                self.assertEqual(f"<Trait name:{trait.name}, type:{trait.type}>", repr(trait))
