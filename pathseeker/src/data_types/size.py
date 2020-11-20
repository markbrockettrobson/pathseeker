import pathseeker.interface.data_types.i_size as i_size


class Size(i_size.ISize):
    def __init__(
        self, name: str, short_name: str, space: int, tall_reach: int, long_reach: int
    ):
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

    def __str__(self) -> str:
        return (
            f"Size: name={self.__name},"
            f" short_name={self.__short_name},"
            f" space={self.__space},"
            f" tall_reach={self.__tall_reach},"
            f" long_reach={self.__long_reach}"
        )
