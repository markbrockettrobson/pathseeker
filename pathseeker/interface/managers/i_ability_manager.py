import abc

import typing
from pathseeker.interface.data_types.i_ability import IAbility


class IAbilityManager(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def name_to_type(name: str) -> IAbility:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_type(short_name: str) -> IAbility:
        pass

    @staticmethod
    @abc.abstractmethod
    def comma_separated_name_list_to_type_list(name_list: str) -> typing.List[IAbility]:
        pass

    @staticmethod
    @abc.abstractmethod
    def comma_separated_short_name_list_to_type_list(short_name_list: str) -> typing.List[IAbility]:
        pass

    @staticmethod
    @abc.abstractmethod
    def ability_score_to_ability_modifier(score: int) -> int:
        pass
