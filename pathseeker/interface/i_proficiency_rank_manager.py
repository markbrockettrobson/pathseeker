import abc

import pathseeker.interface.i_proficiency_rank as i_proficiency_rank


class IProficiencyRankManager(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def name_to_type(name: str) -> i_proficiency_rank.IProficiencyRank:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_type(short_name: str) -> i_proficiency_rank.IProficiencyRank:
        pass
