import abc

from pathseeker.interface.data_types.i_modifier_type import IModifierType


class IModifierTypeManager(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def name_to_type(name: str) -> IModifierType:
        pass

    @staticmethod
    @abc.abstractmethod
    def short_name_to_type(short_name: str) -> IModifierType:
        pass
