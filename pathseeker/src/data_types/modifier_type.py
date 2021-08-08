from pydantic import BaseModel, validator

from pathseeker.src.data_types.validators.string_validators import cant_be_empty, must_be_lowercase


class ModifierType(BaseModel):
    name: str
    duplicate_modifier_type_manager: str

    # validators
    _ensure_name_is_not_empty: classmethod = validator("name", allow_reuse=True)(cant_be_empty)
    _ensure_name_lowercase: classmethod = validator("name", allow_reuse=True)(must_be_lowercase)

    _ensure_duplicate_modifier_type_manager_lowercase: classmethod = validator(
        "duplicate_modifier_type_manager", allow_reuse=True
    )(must_be_lowercase)
