from abc import ABCMeta, abstractmethod

from pathseeker.src.data_types.modifier_type import ModifierType
from pathseeker.interface.modifier.i_duplicate_modifier_type_manager import IDuplicateModifierTypeManager


class IModifierTypeManager(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def name_to_type(name: str) -> ModifierType:
        pass

    @staticmethod
    def name_to_duplicate_modifier_type_manager(name: str) -> IDuplicateModifierTypeManager:
        pass
