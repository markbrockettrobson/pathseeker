from typing import Collection, Callable


def cant_be_empty(value: str) -> str:
    if len(value) <= 0:
        raise ValueError("must not be an empty string")
    return value


def must_be_uppercase(value: str) -> str:
    if not value.isupper():
        raise ValueError("must be uppercase.")
    return value


def must_be_lowercase(value: str) -> str:
    if not value.islower():
        raise ValueError("must be lowercase.")
    return value


def string_value_in_collection(collection: Collection, error_message: str = "must be known value") -> Callable[[str], str]:
    def validator(value: str) -> str:
        if value not in collection:
            raise ValueError(error_message)
        return value
    return validator
