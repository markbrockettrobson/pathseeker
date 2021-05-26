from abc import ABCMeta, abstractmethod

from pathseeker.src.data_types.proficiency_rank import ProficiencyRank


class IProficiencyRankManager(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def name_to_type(name: str) -> ProficiencyRank:
        pass

    @staticmethod
    @abstractmethod
    def short_name_to_type(short_name: str) -> ProficiencyRank:
        pass
