from pathseeker.interface.managers.i_modifier_type_manager import IModifierTypeManager
from pathseeker.src.data_types.modifier_type import ModifierType
from pathseeker.interface.modifier.duplicate_rule.i_duplicate_rule import IDuplicateRule

from unittest.mock import MagicMock


class ModifierTypeManager(IModifierTypeManager):
    HIGHEST_ONLY = MagicMock(spec=IDuplicateRule)
    STACKS = MagicMock(spec=IDuplicateRule)

    __DUPLICATE_RULE = [HIGHEST_ONLY, STACKS]
    __NAME_TO_DUPLICATE_RULE = {
        "stacks": STACKS,
        "highest_only": HIGHEST_ONLY,
    }

    CIRCUMSTANCE = ModifierType(name="circumstance", duplicate_modifier_type_manager="highest_only")
    ITEM = ModifierType(name="item", duplicate_modifier_type_manager="highest_only")
    STATUS = ModifierType(name="status", duplicate_modifier_type_manager="highest_only")
    ABILITY = ModifierType(name="ability", duplicate_modifier_type_manager="highest_only")
    PROFICIENCY = ModifierType(name="proficiency", duplicate_modifier_type_manager="highest_only")
    UNTYPED = ModifierType(name="untyped", duplicate_modifier_type_manager="stacks")

    __MODIFIER_TYPES = [CIRCUMSTANCE, ITEM, STATUS, ABILITY, PROFICIENCY, UNTYPED]
    __NAME_TO_TYPE = {_modifier_type.name: _modifier_type for _modifier_type in __MODIFIER_TYPES}

    @staticmethod
    def name_to_type(name: str) -> ModifierType:
        if name in ModifierTypeManager.__NAME_TO_TYPE:
            return ModifierTypeManager.__NAME_TO_TYPE[name]
        raise Exception(f'Unknown {ModifierType.__name__} name "{name}"')

    @staticmethod
    def name_to_duplicate_rule(name: str) -> IDuplicateRule:
        manager_name = ModifierTypeManager.name_to_type(name=name).duplicate_modifier_type_manager
        if manager_name not in ModifierTypeManager.__NAME_TO_DUPLICATE_RULE:
            raise Exception(f'Unknown {IDuplicateRule.__name__} name "{manager_name}"')
        return ModifierTypeManager.__NAME_TO_DUPLICATE_RULE[manager_name]
