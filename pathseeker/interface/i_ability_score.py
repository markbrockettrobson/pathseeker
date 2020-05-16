import abc


class IAbilityScore(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_short_name(self) -> str:
        pass
