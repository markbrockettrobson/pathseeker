import abc


class IToStringFormatter(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def to_string(class_name: str, **internal_kwargs: str) -> str:
        pass
