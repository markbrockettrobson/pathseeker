from pydantic import BaseModel


class Ability(BaseModel):
    name: str
    short_name: str
