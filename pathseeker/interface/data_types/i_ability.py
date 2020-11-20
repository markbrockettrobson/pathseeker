import abc


class IAbility(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def short_name(self) -> str:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass
