import pathseeker.interface.data_types.i_proficiency_rank as i_proficiency_rank
import pathseeker.src.common.to_string_formatter as to_string_formatter


class ProficiencyRank(i_proficiency_rank.IProficiencyRank):
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

    def __str__(self) -> str:
        return to_string_formatter.ToStringFormatter.to_string(
            class_name=ProficiencyRank.__name__,
            name=self.__name,
            short_name=self.__short_name,
            value=str(self.__value),
        )
