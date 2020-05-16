import abc
import typing

import pathseeker.interface.i_ability_score as i_ability_score


class IAbilityScoreManager(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def name_to_type(name: str) -> i_ability_score.IAbilityScore:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_type(short_name: str) -> i_ability_score.IAbilityScore:
        pass

    @staticmethod
    @abc.abstractmethod
    def comma_separated_name_list_to_type_list(
        name_list: str
    ) -> typing.List[i_ability_score.IAbilityScore]:
        pass

    @staticmethod
    @abc.abstractmethod
    def comma_separated_short_name_list_to_type_list(
        short_name_list: str
    ) -> typing.List[i_ability_score.IAbilityScore]:
        pass

    @staticmethod
    @abc.abstractmethod
    def ability_score_to_ability_modifier(score: int) -> int:
        pass
