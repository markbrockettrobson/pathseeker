from pydantic import BaseModel, validator

from pathseeker.src.data_types.validators.int_validators import cant_be_negative, must_be_multiple_of_five
from pathseeker.src.data_types.validators.string_validators import cant_be_empty, must_be_lowercase, must_be_uppercase


class Size(BaseModel):
    name: str
    short_name: str
    space: int
    tall_reach: int
    long_reach: int

    # validators
    _ensure_name_is_not_empty: classmethod = validator("name", allow_reuse=True)(cant_be_empty)
    _ensure_name_lowercase: classmethod = validator("name", allow_reuse=True)(must_be_lowercase)

    _ensure_short_name_is_not_empty: classmethod = validator("short_name", allow_reuse=True)(cant_be_empty)
    _ensure_short_uppercase: classmethod = validator("short_name", allow_reuse=True)(must_be_uppercase)

    _ensure_space_is_not_negative: classmethod = validator("space", allow_reuse=True)(cant_be_negative)
    _ensure_space_is_multiple_of_five: classmethod = validator("space", allow_reuse=True)(must_be_multiple_of_five)

    _ensure_tall_reach_is_not_negative: classmethod = validator("tall_reach", allow_reuse=True)(cant_be_negative)
    _ensure_tall_reach_is_multiple_of_five: classmethod = validator("tall_reach", allow_reuse=True)(
        must_be_multiple_of_five
    )

    _ensure_long_reach_is_not_negative: classmethod = validator("long_reach", allow_reuse=True)(cant_be_negative)
    _ensure_long_reach_is_multiple_of_five: classmethod = validator("long_reach", allow_reuse=True)(
        must_be_multiple_of_five
    )
