import pathseeker.interface.data_types.i_size as i_size
import pathseeker.interface.managers.i_size_manager as i_size_manager
import pathseeker.src.data_types.size as size


class SizeManager(i_size_manager.ISizeManager):

    TINY = size.Size(name="tiny", short_name="T", space=0, tall_reach=0, long_reach=0)
    SMALL = size.Size(name="small", short_name="S", space=5, tall_reach=5, long_reach=5)
    MEDIUM = size.Size(
        name="medium", short_name="M", space=5, tall_reach=5, long_reach=5
    )
    LARGE = size.Size(
        name="large", short_name="L", space=10, tall_reach=10, long_reach=5
    )
    HUGE = size.Size(
        name="huge", short_name="H", space=15, tall_reach=15, long_reach=10
    )
    GARGANTUAN = size.Size(
        name="gargantuan", short_name="G", space=20, tall_reach=20, long_reach=15
    )

    SIZES = [TINY, SMALL, MEDIUM, LARGE, HUGE, GARGANTUAN]
    __NAME_TO_SIZE = {_size.name: _size for _size in SIZES}
    __SHORT_NAME_TO_SIZE = {_size.short_name: _size for _size in SIZES}

    @staticmethod
    def name_to_size(name: str) -> i_size.ISize:
        if name in SizeManager.__NAME_TO_SIZE:
            return SizeManager.__NAME_TO_SIZE[name]
        raise Exception(f'Unknown size name "{name}"')

    @staticmethod
    def short_name_to_size(short_name: str) -> i_size.ISize:
        if short_name in SizeManager.__SHORT_NAME_TO_SIZE:
            return SizeManager.__SHORT_NAME_TO_SIZE[short_name]
        raise Exception(f'Unknown size short name "{short_name}"')
