from typing import Collection

from pathseeker.interface.modifier.duplicate_rule.i_duplicate_rule import IDuplicateRule
from pathseeker.interface.modifier.i_modifier import IModifier


class Stacks(IDuplicateRule[int]):
    @staticmethod
    def apply_rule(modifiers: Collection[IModifier[int]]) -> Collection[IModifier[int]]:
        return set(modifiers)
