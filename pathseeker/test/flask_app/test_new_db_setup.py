from unittest import TestCase

from pathseeker.src.database.db_table_list import TABLES
from pathseeker.src.flask_app.app_factory import DATABASE
from pathseeker.src.flask_app.new_db_setup import main as new_db_setup_main


class TestNewDbSetup(TestCase):
    def test_db_created(self):
        new_db_setup_main()
        database = DATABASE
        self.assertIsNotNone(database)
        result = database.session.execute("SHOW TABLES;")

        tables_names = {r["Tables_in_pathseeker"] for r in result}

        for table in TABLES:
            self.assertIn(table.__tablename__, tables_names)
