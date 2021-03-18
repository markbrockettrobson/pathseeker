import abc

from pathseeker.interface.data_types.i_proficiency_rank import IProficiencyRank


class IProficiencyRankManager(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def name_to_type(name: str) -> IProficiencyRank:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_type(short_name: str) -> IProficiencyRank:
        pass
