import typing

import pathseeker.interface.i_ability_score as i_ability_score
import pathseeker.interface.i_ability_score_manager as i_ability_score_manager
import pathseeker.src.ability_score as ability_score


class AbilityScoreManager(i_ability_score_manager.IAbilityScoreManager):

    STRENGTH = ability_score.AbilityScore("strength", "STR")
    DEXTERITY = ability_score.AbilityScore("dexterity", "DEX")
    CONSTITUTION = ability_score.AbilityScore("constitution", "CON")
    INTELLIGENCE = ability_score.AbilityScore("intelligence", "INT")
    WISDOM = ability_score.AbilityScore("wisdom", "WIS")
    CHARISMA = ability_score.AbilityScore("charisma", "CHA")
    FREE = ability_score.AbilityScore("free", "FRE")

    ABILITY_SCORES = [
        STRENGTH,
        DEXTERITY,
        CONSTITUTION,
        INTELLIGENCE,
        WISDOM,
        CHARISMA,
        FREE,
    ]
    __NAME_TO_TYPE = {
        _ability_score.get_name(): _ability_score for _ability_score in ABILITY_SCORES
    }
    __SHORT_NAME_TO_TYPE = {
        _ability_score.get_short_name(): _ability_score
        for _ability_score in ABILITY_SCORES
    }

    @staticmethod
    def name_to_short_name(name: str) -> str:
        return AbilityScoreManager.name_to_type(name).get_short_name()

    @staticmethod
    def short_name_to_name(short_name: str) -> str:
        return AbilityScoreManager.short_name_to_type(short_name).get_name()

    @staticmethod
    def name_to_type(name: str) -> i_ability_score.IAbilityScore:
        if name in AbilityScoreManager.__NAME_TO_TYPE:
            return AbilityScoreManager.__NAME_TO_TYPE[name]
        raise Exception(f'Unknown ability score name "{name}"')

    @staticmethod
    def short_name_to_type(short_name: str) -> i_ability_score.IAbilityScore:
        if short_name in AbilityScoreManager.__SHORT_NAME_TO_TYPE:
            return AbilityScoreManager.__SHORT_NAME_TO_TYPE[short_name]
        raise Exception(f'Unknown ability score short name "{short_name}"')

    @staticmethod
    def comma_separated_name_list_to_type_list(
        name_list: str
    ) -> typing.List[i_ability_score.IAbilityScore]:
        if name_list == "":
            return []
        return [
            AbilityScoreManager.name_to_type(name) for name in str.split(name_list, ",")
        ]

    @staticmethod
    def comma_separated_short_name_list_to_type_list(
        short_name_list: str
    ) -> typing.List[i_ability_score.IAbilityScore]:
        if short_name_list == "":
            return []
        return [
            AbilityScoreManager.short_name_to_type(short_name)
            for short_name in str.split(short_name_list, ",")
        ]

    @staticmethod
    def ability_score_to_ability_modifier(score: int) -> int:
        return (score - 10) // 2
