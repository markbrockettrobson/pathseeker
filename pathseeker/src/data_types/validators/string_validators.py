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
