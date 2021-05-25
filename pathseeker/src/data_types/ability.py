import pydantic

from pathseeker.src.data_types.validators.string_validators import cant_be_empty, must_be_lowercase, must_be_uppercase


class Ability(pydantic.BaseModel):
    name: str
    short_name: str

    # validators
    _ensure_name_is_not_empty: classmethod = pydantic.validator("name", allow_reuse=True)(cant_be_empty)
    _ensure_name_lowercase: classmethod = pydantic.validator("name", allow_reuse=True)(must_be_lowercase)
    _ensure_short_name_is_not_empty: classmethod = pydantic.validator("short_name", allow_reuse=True)(cant_be_empty)
    _ensure_short_uppercase: classmethod = pydantic.validator("short_name", allow_reuse=True)(must_be_uppercase)