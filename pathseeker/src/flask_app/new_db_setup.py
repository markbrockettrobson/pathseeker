from pathlib import Path

from pathseeker.src.database.db_table_list import TABLES
from pathseeker.src.flask_app.app_factory import DATABASE
from pathseeker.src.logging.logging_manager import LoggingManager

LOGGER = LoggingManager.get_logger(Path(__file__).name)


def main():
    LOGGER.info("Creating DB tables")
    LOGGER.info("Creating the following tables:")
    for table in TABLES:
        LOGGER.info(table.__name__)

    DATABASE.create_all()
    LOGGER.info("DB tables created")


if __name__ == "__main__":  # pragma: no cover
    main()
