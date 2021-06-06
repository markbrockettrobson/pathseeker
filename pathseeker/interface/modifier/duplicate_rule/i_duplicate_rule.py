from abc import ABCMeta, abstractmethod
from typing import Collection, Generic, TypeVar

from pathseeker.interface.modifier.i_modifier import IModifier

ModifierValueType = TypeVar("ModifierValueType")


class IDuplicateRule(Generic[ModifierValueType], metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def apply_rule(modifiers: Collection[IModifier[ModifierValueType]]) -> Collection[IModifier[ModifierValueType]]:
        pass
