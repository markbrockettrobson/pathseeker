from pathseeker.interface.data_types.i_modifier_type import IModifierType
from pathseeker.interface.managers.i_modifier_type_manager import IModifierTypeManager
from pathseeker.src.data_types.modifier_type import ModifierType


class ModifierTypeManager(IModifierTypeManager):

    CIRCUMSTANCE = ModifierType(name="circumstance", short_name="C")
    ITEM = ModifierType(name="item", short_name="I")
    PROFICIENCY = ModifierType(name="proficiency", short_name="P")
    STATUS = ModifierType(name="status", short_name="S")
    UNTYPED = ModifierType(name="untyped", short_name="U")

    __MODIFIER_TYPES = [CIRCUMSTANCE, ITEM, PROFICIENCY, STATUS, UNTYPED]
    __NAME_TO_TYPE = {_ability_score.name: _ability_score for _ability_score in __MODIFIER_TYPES}
    __SHORT_NAME_TO_TYPE = {_ability_score.short_name: _ability_score for _ability_score in __MODIFIER_TYPES}

    @staticmethod
    def name_to_type(name: str) -> IModifierType:
        if name in ModifierTypeManager.__NAME_TO_TYPE:
            return ModifierTypeManager.__NAME_TO_TYPE[name]
        raise Exception(f'Unknown {ModifierType.__name__} name "{name}"')

    @staticmethod
    def short_name_to_type(short_name: str) -> IModifierType:
        if short_name in ModifierTypeManager.__SHORT_NAME_TO_TYPE:
            return ModifierTypeManager.__SHORT_NAME_TO_TYPE[short_name]
        raise Exception(f'Unknown {ModifierType.__name__} short name "{short_name}"')
