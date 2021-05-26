from pathseeker.interface.managers.i_size_manager import ISizeManager
from pathseeker.src.data_types.size import Size


class SizeManager(ISizeManager):

    TINY = Size(name="tiny", short_name="T", space=0, tall_reach=0, long_reach=0)
    SMALL = Size(name="small", short_name="S", space=5, tall_reach=5, long_reach=5)
    MEDIUM = Size(name="medium", short_name="M", space=5, tall_reach=5, long_reach=5)
    LARGE = Size(name="large", short_name="L", space=10, tall_reach=10, long_reach=5)
    HUGE = Size(name="huge", short_name="H", space=15, tall_reach=15, long_reach=10)
    GARGANTUAN = Size(name="gargantuan", short_name="G", space=20, tall_reach=20, long_reach=15)

    __SIZES = [TINY, SMALL, MEDIUM, LARGE, HUGE, GARGANTUAN]
    __NAME_TO_SIZE = {_size.name: _size for _size in __SIZES}
    __SHORT_NAME_TO_SIZE = {_size.short_name: _size for _size in __SIZES}

    @staticmethod
    def name_to_size(name: str) -> Size:
        if name in SizeManager.__NAME_TO_SIZE:
            return SizeManager.__NAME_TO_SIZE[name]
        raise Exception(f'Unknown {Size.__name__} name "{name}"')

    @staticmethod
    def short_name_to_size(short_name: str) -> Size:
        if short_name in SizeManager.__SHORT_NAME_TO_SIZE:
            return SizeManager.__SHORT_NAME_TO_SIZE[short_name]
        raise Exception(f'Unknown {Size.__name__} short name "{short_name}"')
