import abc


class ISize(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_short_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_space(self) -> int:
        pass

    @abc.abstractmethod
    def get_tall_reach(self) -> int:
        pass

    @abc.abstractmethod
    def get_long_reach(self) -> int:
        pass
