from pydantic import BaseModel, validator

from pathseeker.src.data_types.validators.int_validators import cant_be_negative
from pathseeker.src.data_types.validators.string_validators import cant_be_empty, must_be_lowercase, must_be_uppercase


class ProficiencyRank(BaseModel):
    name: str
    short_name: str
    value: int
    add_level: bool

    # validators
    _ensure_name_is_not_empty: classmethod = validator("name", allow_reuse=True)(cant_be_empty)
    _ensure_name_lowercase: classmethod = validator("name", allow_reuse=True)(must_be_lowercase)

    _ensure_short_name_is_not_empty: classmethod = validator("short_name", allow_reuse=True)(cant_be_empty)
    _ensure_short_uppercase: classmethod = validator("short_name", allow_reuse=True)(must_be_uppercase)

    _ensure_value_is_not_negative: classmethod = validator("value", allow_reuse=True)(cant_be_negative)
