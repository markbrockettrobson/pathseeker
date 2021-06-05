from unittest import TestCase, skipIf

from pathseeker.src.config.test_config import RUN_SQL_INTEGRATION_TEST
from pathseeker.src.database.db_table_list import TABLES
from pathseeker.src.database.new_db_setup import main as new_db_setup_main
from pathseeker.src.flask_app.app_factory import DATABASE


class TestNewDbSetup(TestCase):
    @skipIf(not RUN_SQL_INTEGRATION_TEST, "Sql db needed for test")
    def test_db_tables_created(self):
        new_db_setup_main()
        database = DATABASE
        self.assertIsNotNone(database)
        result = database.session.execute("SHOW TABLES;")

        tables_names = {r["Tables_in_pathseeker"] for r in result}

        for table in TABLES:
            self.assertIn(table.__tablename__, tables_names)
