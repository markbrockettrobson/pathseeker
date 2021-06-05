from pathlib import Path

from pathseeker.src.config.config_helper import get_environ_bool, get_environ_pos_int, get_environ_str
from pathseeker.src.logging.logging_manager import LoggingManager

LOGGER = LoggingManager.get_logger(Path(__file__).name)

__PATHSEEKER_FLASK_DEBUG_ENVIRON = "PATHSEEKER_FLASK_DEBUG"
FLASK_DEBUG = get_environ_bool(environ_name=__PATHSEEKER_FLASK_DEBUG_ENVIRON, default_value=True, logger=LOGGER)

__PATHSEEKER_FLASK_HOST_ENVIRON = "PATHSEEKER_FLASK_HOST"
FLASK_HOST = get_environ_str(environ_name=__PATHSEEKER_FLASK_HOST_ENVIRON, default_value="localhost", logger=LOGGER)

__PATHSEEKER_FLASK_PORT_ENVIRON = "PATHSEEKER_FLASK_PORT"
FLASK_PORT = get_environ_pos_int(environ_name=__PATHSEEKER_FLASK_PORT_ENVIRON, default_value=5000, logger=LOGGER)
