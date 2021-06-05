from pydantic import BaseModel, validator

from pathseeker.src.data_types.validators.int_validators import cant_be_negative
from pathseeker.src.data_types.validators.string_validators import cant_be_empty, must_be_lowercase, must_be_uppercase


class ModifierType(BaseModel):
    name: str

    # validators
    _ensure_name_is_not_empty: classmethod = validator("name", allow_reuse=True)(cant_be_empty)
    _ensure_name_lowercase: classmethod = validator("name", allow_reuse=True)(must_be_lowercase)
