from logging import DEBUG, INFO, WARNING, Formatter, Logger, StreamHandler, getLogger
from sys import stderr, stdout
from typing import Optional

import pathseeker
from pathseeker.interface.logging.i_logging_manager import ILoggingManager
from pathseeker.src.logging.logging_filter import LevelFilter


class LoggingManager(ILoggingManager):
    __LOGGER_CONFIGURED = False
    __ROOT_NAME = pathseeker.__name__

    @staticmethod
    def get_logger(logger_name: str) -> Logger:
        LoggingManager._setup_logger_if_not_configured()

        logger = getLogger(f"{LoggingManager.__ROOT_NAME}.{logger_name}")
        return logger

    @staticmethod
    def get_child_logger(logger_name: str, parent_logger: Optional[Logger] = None) -> Logger:
        if logger_name == "":
            raise ValueError('Child logger can not have "" as a name.')

        LoggingManager._setup_logger_if_not_configured()

        if parent_logger is not None:
            return parent_logger.getChild(logger_name)
        return LoggingManager.get_logger(logger_name)

    @staticmethod
    def _setup_logger_if_not_configured():
        if not LoggingManager.__LOGGER_CONFIGURED:
            LoggingManager._setup_logger(LoggingManager.__ROOT_NAME)

    @staticmethod
    def _setup_logger(root_name: str):
        logger = getLogger(root_name)
        logger.setLevel(INFO)
        formatter = Formatter("%(asctime)s | %(name)-40s | %(levelname)-10s | %(message)s")

        stdout_log_filter = LevelFilter({INFO, DEBUG})
        stdout_stream_handler = StreamHandler(stdout)
        stdout_stream_handler.setLevel(INFO)
        stdout_stream_handler.setFormatter(formatter)
        stdout_stream_handler.addFilter(stdout_log_filter)

        stderr_stream_handler = StreamHandler(stderr)
        stderr_stream_handler.setLevel(WARNING)
        stderr_stream_handler.setFormatter(formatter)

        logger.addHandler(stdout_stream_handler)
        logger.addHandler(stderr_stream_handler)

        LoggingManager.__LOGGER_CONFIGURED = True
