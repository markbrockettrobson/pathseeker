import abc


class IToStringFormatter(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def to_string(class_name: str, **internal_value: str) -> str:
        pass
