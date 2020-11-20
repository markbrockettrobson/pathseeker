import pathseeker.interface.data_types.i_size as i_size
import pathseeker.src.common.to_string_formatter as to_string_formatter


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
        return to_string_formatter.ToStringFormatter.to_string(
            class_name=Size.__name__,
            name=self.__name,
            short_name=self.__short_name,
            space=str(self.__space),
            tall_reach=str(self.__tall_reach),
            long_reach=str(self.__long_reach),
        )
