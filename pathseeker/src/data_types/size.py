from pathseeker.interface.data_types.i_size import ISize
from pathseeker.interface.common.i_data_type import IDataType
from pathseeker.src.common.data_type_base import DataTypeBase


class Size(ISize, IDataType, DataTypeBase):
    def __init__(self, name: str, short_name: str, space: int, tall_reach: int, long_reach: int):
        self.__name = name
        self.__short_name = short_name
        self.__space = space
        self.__tall_reach = tall_reach
        self.__long_reach = long_reach

    @property
    def name(self) -> str:
        return self.__name

    @property
    def short_name(self) -> str:
        return self.__short_name

    @property
    def space(self) -> int:
        return self.__space

    @property
    def tall_reach(self) -> int:
        return self.__tall_reach

    @property
    def long_reach(self) -> int:
        return self.__long_reach
