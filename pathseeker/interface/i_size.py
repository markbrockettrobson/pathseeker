import abc


class ISize(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def short_name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def space(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def tall_reach(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def long_reach(self) -> int:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass
