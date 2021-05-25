from string import ascii_letters

from hypothesis import strategies

from pathseeker.src.data_types.ability import Ability


@strategies.composite
def ability_strategy(
    draw,
    alphabet: str = ascii_letters,
    min_name_length: int = 1,
    max_name_length: int = 10,
    min_short_name_length: int = 1,
    max_short_name_length: int = 10,
):
    name = draw(strategies.text(alphabet=alphabet, min_size=min_name_length, max_size=max_name_length))
    short_name = draw(
        strategies.text(alphabet=alphabet, min_size=min_short_name_length, max_size=max_short_name_length)
    )
    return Ability(name=name, short_name=short_name)
