from pathlib import Path

from pathseeker.src.config.config_helper import get_environ_str
from pathseeker.src.logging.logging_manager import LoggingManager

LOGGER = LoggingManager.get_logger(Path(__file__).name)

__MYSQL_DATABASE_URL = "PATHSEEKER_MYSQL_DATABASE_URL"
MYSQL_DATABASE_URL = get_environ_str(
    environ_name=__MYSQL_DATABASE_URL, default_value="localhost/pathseeker", logger=LOGGER
)

__MYSQL_DATABASE_USERNAME = "PATHSEEKER_MYSQL_DATABASE_USERNAME"
MYSQL_DATABASE_USERNAME = get_environ_str(
    environ_name=__MYSQL_DATABASE_USERNAME, default_value="Gg6zGq5Ld8JG7jrxYYSz74abM285nqjf", logger=LOGGER
)

__MYSQL_DATABASE_PASSWORD = "PATHSEEKER_MYSQL_DATABASE_PASSWORD"
MYSQL_DATABASE_PASSWORD = get_environ_str(
    environ_name=__MYSQL_DATABASE_PASSWORD,
    default_value="ESqqUfg6xEreBMpmNn7qb3SqxBtsDUzJ",
    hide_value=True,
    logger=LOGGER,
)

MYSQL_CONNECTION_STRING = f"mysql://{MYSQL_DATABASE_USERNAME}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_URL}"
