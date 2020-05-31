import pathseeker.interface.i_proficiency_rank as i_proficiency_rank


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
        return (
            f"ProficiencyRank: name={self.__name},"
            f" short_name={self.__short_name},"
            f" value={self.__value}"
        )
