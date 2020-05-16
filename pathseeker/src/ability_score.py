import pathseeker.interface.i_ability_score as i_ability_score


class AbilityScore(i_ability_score.IAbilityScore):
    def __init__(self, name: str, short_name: str):
        self.__name = name
        self.__short_name = short_name

    def get_name(self) -> str:
        return self.__name

    def get_short_name(self) -> str:
        return self.__short_name

    def __str__(self) -> str:
        return f"AbilityScore: name={self.__name}, short_name={self.__short_name}"
