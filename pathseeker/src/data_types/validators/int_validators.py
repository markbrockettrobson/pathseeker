def cant_be_negative(value: int) -> int:
    if value < 0:
        raise ValueError("Must not be negative.")
    return value


def must_be_multiple_of_five(value: int) -> int:
    if value % 5 != 0:
        raise ValueError("Must be a multiple of five.")
    return value
