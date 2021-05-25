from pathseeker.interface.managers.i_proficiency_rank_manager import IProficiencyRankManager
from pathseeker.src.data_types.proficiency_rank import ProficiencyRank


class ProficiencyRankManager(IProficiencyRankManager):

    UNTRAINED = ProficiencyRank(name="untrained", short_name="U", value=0, add_level=False)
    TRAINED = ProficiencyRank(name="trained", short_name="T", value=2, add_level=True)
    EXPERT = ProficiencyRank(name="expert", short_name="E", value=4, add_level=True)
    MASTER = ProficiencyRank(name="master", short_name="M", value=6, add_level=True)
    LEGENDARY = ProficiencyRank(name="legendary", short_name="L", value=8, add_level=True)

    __RANKS = [UNTRAINED, TRAINED, EXPERT, MASTER, LEGENDARY]
    __NAME_TO_RANK = {_rank.name: _rank for _rank in __RANKS}
    __SHORT_NAME_TO_RANK = {_rank.short_name: _rank for _rank in __RANKS}

    @staticmethod
    def name_to_type(name: str) -> ProficiencyRank:
        if name in ProficiencyRankManager.__NAME_TO_RANK:
            return ProficiencyRankManager.__NAME_TO_RANK[name]
        raise Exception(f'Unknown {ProficiencyRank.__name__} name "{name}"')

    @staticmethod
    def short_name_to_type(short_name: str) -> ProficiencyRank:
        if short_name in ProficiencyRankManager.__SHORT_NAME_TO_RANK:
            return ProficiencyRankManager.__SHORT_NAME_TO_RANK[short_name]
        raise Exception(f'Unknown {ProficiencyRank.__name__} short name "{short_name}"')
