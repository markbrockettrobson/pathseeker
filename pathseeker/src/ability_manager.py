import typing

import pathseeker.interface.i_ability as i_ability
import pathseeker.interface.i_ability_manager as i_ability_manager
import pathseeker.src.ability as ability


class AbilityManager(i_ability_manager.IAbilityManager):

    STRENGTH = ability.Ability(name="strength", short_name="STR")
    DEXTERITY = ability.Ability(name="dexterity", short_name="DEX")
    CONSTITUTION = ability.Ability(name="constitution", short_name="CON")
    INTELLIGENCE = ability.Ability(name="intelligence", short_name="INT")
    WISDOM = ability.Ability(name="wisdom", short_name="WIS")
    CHARISMA = ability.Ability(name="charisma", short_name="CHA")
    FREE = ability.Ability(name="free", short_name="FRE")

    ABILITIES = [
        STRENGTH,
        DEXTERITY,
        CONSTITUTION,
        INTELLIGENCE,
        WISDOM,
        CHARISMA,
        FREE,
    ]
    __NAME_TO_TYPE = {
        _ability_score.name: _ability_score for _ability_score in ABILITIES
    }
    __SHORT_NAME_TO_TYPE = {
        _ability_score.short_name: _ability_score for _ability_score in ABILITIES
    }

    @staticmethod
    def name_to_type(name: str) -> i_ability.IAbility:
        if name in AbilityManager.__NAME_TO_TYPE:
            return AbilityManager.__NAME_TO_TYPE[name]
        raise Exception(f'Unknown ability name "{name}"')

    @staticmethod
    def short_name_to_type(short_name: str) -> i_ability.IAbility:
        if short_name in AbilityManager.__SHORT_NAME_TO_TYPE:
            return AbilityManager.__SHORT_NAME_TO_TYPE[short_name]
        raise Exception(f'Unknown ability short name "{short_name}"')

    @staticmethod
    def comma_separated_name_list_to_type_list(
        name_list: str
    ) -> typing.List[i_ability.IAbility]:
        if name_list == "":
            return []
        return [AbilityManager.name_to_type(name) for name in str.split(name_list, ",")]

    @staticmethod
    def comma_separated_short_name_list_to_type_list(
        short_name_list: str
    ) -> typing.List[i_ability.IAbility]:
        if short_name_list == "":
            return []
        return [
            AbilityManager.short_name_to_type(short_name)
            for short_name in str.split(short_name_list, ",")
        ]

    @staticmethod
    def ability_score_to_ability_modifier(score: int) -> int:
        return (score - 10) // 2
