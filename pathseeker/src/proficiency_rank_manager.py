import pathseeker.interface.i_proficiency_rank as i_proficiency_rank
import pathseeker.interface.i_proficiency_rank_manager as i_proficiency_rank_manager
import pathseeker.src.proficiency_rank as proficiency_rank


class ProficiencyRankManager(i_proficiency_rank_manager.IProficiencyRankManager):

    UNTRAINED = proficiency_rank.ProficiencyRank(
        name="untrained", short_name="U", value=0
    )
    TRAINED = proficiency_rank.ProficiencyRank(name="trained", short_name="T", value=2)
    EXPERT = proficiency_rank.ProficiencyRank(name="expert", short_name="E", value=4)
    MASTER = proficiency_rank.ProficiencyRank(name="master", short_name="M", value=6)
    LEGENDARY = proficiency_rank.ProficiencyRank(
        name="legendary", short_name="L", value=8
    )

    RANKS = [UNTRAINED, TRAINED, EXPERT, MASTER, LEGENDARY]
    __NAME_TO_RANK = {_rank.name: _rank for _rank in RANKS}
    __SHORT_NAME_TO_RANK = {_rank.short_name: _rank for _rank in RANKS}

    @staticmethod
    def name_to_type(name: str) -> i_proficiency_rank.IProficiencyRank:
        if name in ProficiencyRankManager.__NAME_TO_RANK:
            return ProficiencyRankManager.__NAME_TO_RANK[name]
        raise Exception(f'Unknown proficiency rank name "{name}"')

    @staticmethod
    def short_name_to_type(short_name: str) -> i_proficiency_rank.IProficiencyRank:
        if short_name in ProficiencyRankManager.__SHORT_NAME_TO_RANK:
            return ProficiencyRankManager.__SHORT_NAME_TO_RANK[short_name]
        raise Exception(f'Unknown proficiency rank short name "{short_name}"')
