from logging import Logger
from os import environ
from typing import Optional

TRUE_VALUES = {"True", "T", "true", "t", "1"}


def get_environ_bool(environ_name: str, default_value: Optional[bool] = None, logger: Optional[Logger] = None) -> bool:
    if environ_name in environ:
        if logger is not None:
            logger.info("environmental variables, %s set to %s", environ_name, environ[environ_name])
        return environ[environ_name] in TRUE_VALUES
    if default_value is None:
        raise ValueError("must set %s" % environ_name)
    return default_value


def get_environ_str(
    environ_name: str,
    default_value: Optional[str] = None,
    can_be_empty: bool = False,
    hide_value: bool = False,
    logger: Optional[Logger] = None,
) -> str:
    if environ_name in environ:
        if not can_be_empty and len(environ[environ_name]) == 0:
            raise ValueError("%s set to empty string" % environ_name)
        if logger is not None:
            logger.info(
                "environmental variables, %s set to %s",
                environ_name,
                "*" * len(environ[environ_name]) if hide_value else environ[environ_name],
            )
        return environ[environ_name]
    if default_value is None:
        raise ValueError("must set %s" % environ_name)
    return default_value


def get_environ_pos_int(environ_name: str, default_value: Optional[int] = None, logger: Optional[Logger] = None) -> int:
    if environ_name in environ:
        if environ[environ_name].isdigit():
            if logger is not None:
                logger.info("environmental variables, %s set to %s", environ_name, environ[environ_name])
            return int(environ[environ_name])
        raise ValueError(f"Non int value for {environ_name}, was {environ[environ_name]}")
    if default_value is None:
        raise ValueError("must set %s" % environ_name)
    return default_value
