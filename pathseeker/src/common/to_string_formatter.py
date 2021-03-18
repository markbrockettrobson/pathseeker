from pathseeker.interface.common.i_to_string_formatter import IToStringFormatter


class ToStringFormatter(IToStringFormatter):
    @staticmethod
    def to_string(class_name: str, **internal_kwargs: str) -> str:
        internal_value_string = ", ".join(f"{param}={value}" for param, value in internal_kwargs.items())
        return f"{class_name}: {internal_value_string}"
