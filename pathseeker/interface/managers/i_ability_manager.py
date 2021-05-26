from abc import ABCMeta, abstractmethod

from pathseeker.src.data_types.ability import Ability


class IAbilityManager(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def name_to_type(name: str) -> Ability:
        pass

    @staticmethod
    @abstractmethod
    def short_name_to_type(short_name: str) -> Ability:
        pass

    @staticmethod
    @abstractmethod
    def ability_score_to_ability_modifier(score: int) -> int:
        pass
