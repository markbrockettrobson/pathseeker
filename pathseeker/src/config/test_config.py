from pathlib import Path

from pathseeker.src.config.config_helper import get_environ_bool
from pathseeker.src.logging.logging_manager import LoggingManager

LOGGER = LoggingManager.get_logger(Path(__file__).name)

__RUN_SQL_INTEGRATION_TEST = "PATHSEEKER_RUN_SQL_INTEGRATION_TEST"
RUN_SQL_INTEGRATION_TEST = get_environ_bool(environ_name=__RUN_SQL_INTEGRATION_TEST, default_value=False, logger=LOGGER)
