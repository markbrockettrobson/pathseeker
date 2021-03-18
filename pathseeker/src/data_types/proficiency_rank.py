from pathseeker.interface.data_types.i_proficiency_rank import IProficiencyRank
from pathseeker.src.common.data_type_base import DataTypeBase


class ProficiencyRank(IProficiencyRank, DataTypeBase):
    def __init__(self, name: str, short_name: str, value: int):
        self.__name = name
        self.__short_name = short_name
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def short_name(self) -> str:
        return self.__short_name

    @property
    def value(self) -> int:
        return self.__value
