import typing
from random import randint
class GameUtils:
    def get_random_pos(self, width_limit:int, height_limit:int) -> typing.Tuple[int, int]:
        return randint(0, width_limit), randint(0, height_limit)