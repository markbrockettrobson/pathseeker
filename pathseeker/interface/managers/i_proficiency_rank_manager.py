import abc

from pathseeker.src.data_types.proficiency_rank import ProficiencyRank


class IProficiencyRankManager(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def name_to_type(name: str) -> ProficiencyRank:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_type(short_name: str) -> ProficiencyRank:
        pass
