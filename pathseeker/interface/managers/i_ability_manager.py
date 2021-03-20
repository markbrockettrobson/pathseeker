import abc

from pathseeker.src.data_types.ability import Ability


class IAbilityManager(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def name_to_type(name: str) -> Ability:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_type(short_name: str) -> Ability:
        pass

    @staticmethod
    @abc.abstractmethod
    def ability_score_to_ability_modifier(score: int) -> int:
        pass
