import pathseeker.interface.data_types.i_ability as i_ability


class Ability(i_ability.IAbility):
    def __init__(self, name: str, short_name: str):
        self.__name = name
        self.__short_name = short_name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def short_name(self) -> str:
        return self.__short_name

    def __str__(self) -> str:
        return f"Ability: name={self.__name}, short_name={self.__short_name}"
