import pathseeker.interface.i_size as i_size


class Size(i_size.ISize):
    def __init__(
            self,
            name: str,
            short_name: str,
            space: int,
            tall_reach: int,
            long_reach: int,
    ):
        self.__name = name
        self.__short_name = short_name
        self.__space = space
        self.__tall_reach = tall_reach
        self.__long_reach = long_reach

    def get_name(self) -> str:
        return self.__name

    def get_short_name(self) -> str:
        return self.__short_name

    def get_space(self) -> int:
        return self.__space

    def get_tall_reach(self) -> int:
        return self.__tall_reach

    def get_long_reach(self) -> int:
        return self.__long_reach

    def __str__(self) -> str:
        return f"Size: name={self.__name}," \
               f" short_name={self.__short_name}," \
               f" space={self.__space}," \
               f" tall_reach={self.__tall_reach}," \
               f" long_reach={self.__long_reach}" \
