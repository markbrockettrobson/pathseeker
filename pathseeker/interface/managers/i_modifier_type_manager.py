from abc import ABCMeta, abstractmethod

from pathseeker.interface.modifier.duplicate_rule.i_duplicate_rule import IDuplicateRule
from pathseeker.src.data_types.modifier_type import ModifierType


class IModifierTypeManager(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def name_to_type(name: str) -> ModifierType:
        pass

    @staticmethod
    @abstractmethod
    def name_to_duplicate_rule(name: str) -> IDuplicateRule:
        pass
