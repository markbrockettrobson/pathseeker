import pathseeker.interface.common.i_to_string_formatter as i_to_string_formatter


class ToStringFormatter(i_to_string_formatter.IToStringFormatter):
    @staticmethod
    def to_string(class_name: str, **internal_value: str) -> str:
        internal_value_string = ", ".join(
            f"{param}={value}" for param, value in internal_value.items()
        )
        return f"{class_name}: {internal_value_string}"
