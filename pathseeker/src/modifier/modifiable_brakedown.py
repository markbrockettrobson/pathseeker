from typing import Iterable, TypeVar

from pathseeker.interface.modifier.i_modifiable_brakedown import IModifiableBrakedown

ModifierValueType = TypeVar("ModifierValueType")


class ModifiableBrakedown(IModifiableBrakedown[ModifierValueType]):
    def __init__(
        self,
        name: str,
        value: ModifierValueType,
        priority: int = 0,
        modifiable_brakedowns: Iterable[IModifiableBrakedown[ModifierValueType]] = None,
    ):
        if modifiable_brakedowns is not None:
            self._modifiable_brakedowns = list(modifiable_brakedowns)
            self._modifiable_brakedowns.sort(key=lambda x: x.priority)
        else:
            self._modifiable_brakedowns = []

        self._name = name
        self._value = value
        self._priority = priority

    def get_simple_string(self) -> str:
        value_line = "%4s %s" % (self._value, self._name)
        modifiable_lines = ["%4s %s" % (brakedown.value, brakedown.name) for brakedown in self._modifiable_brakedowns]

        return value_line + ("\n\t" if len(modifiable_lines) else "") + "\n\t".join(modifiable_lines)

    def get_detailed_string(self) -> str:
        value_line = "%4s %s" % (self._value, self._name)
        modifiable_lines = [
            brakedown.get_detailed_string().replace("\n", "\n\t\t") for brakedown in self._modifiable_brakedowns
        ]

        return value_line + ("\n\t" if len(modifiable_lines) else "") + "\n\t".join(modifiable_lines)

    @property
    def value(self) -> ModifierValueType:
        return self._value

    @property
    def name(self) -> str:
        return self._name

    @property
    def priority(self) -> int:
        return self._priority
