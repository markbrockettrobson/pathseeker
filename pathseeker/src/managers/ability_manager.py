from pathseeker.interface.managers.i_ability_manager import IAbilityManager
from pathseeker.src.data_types.ability import Ability


class AbilityManager(IAbilityManager):

    STRENGTH = Ability(name="strength", short_name="STR")
    DEXTERITY = Ability(name="dexterity", short_name="DEX")
    CONSTITUTION = Ability(name="constitution", short_name="CON")
    INTELLIGENCE = Ability(name="intelligence", short_name="INT")
    WISDOM = Ability(name="wisdom", short_name="WIS")
    CHARISMA = Ability(name="charisma", short_name="CHA")

    __ABILITIES = [STRENGTH, DEXTERITY, CONSTITUTION, INTELLIGENCE, WISDOM, CHARISMA]
    __NAME_TO_TYPE = {_ability_score.name: _ability_score for _ability_score in __ABILITIES}
    __SHORT_NAME_TO_TYPE = {_ability_score.short_name: _ability_score for _ability_score in __ABILITIES}

    @staticmethod
    def name_to_type(name: str) -> Ability:
        if name in AbilityManager.__NAME_TO_TYPE:
            return AbilityManager.__NAME_TO_TYPE[name]
        raise Exception(f'Unknown {Ability.__name__} name "{name}"')

    @staticmethod
    def short_name_to_type(short_name: str) -> Ability:
        if short_name in AbilityManager.__SHORT_NAME_TO_TYPE:
            return AbilityManager.__SHORT_NAME_TO_TYPE[short_name]
        raise Exception(f'Unknown {Ability.__name__} short name "{short_name}"')

    @staticmethod
    def ability_score_to_ability_modifier(score: int) -> int:
        return (score - 10) // 2
