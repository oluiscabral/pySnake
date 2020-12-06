from pySnake.element import Element
from pySnake.display import Display
import typing
from pygame import Surface
from pySnake.displays.game_display.game import SnakeGame
from pySnake.config import GeneralConfig



class GameDisplay(Display):
    def __init__(self, config: GeneralConfig, parent: Display, active: bool):
        surface = config.get_surface()
        super().__init__(config, parent, [0,0], surface.get_size(), active)
        child_elements: typing.List[Display] = [
            SnakeGame(config, self, [0, 60], [surface.get_width(), 440])
        ]
        self.add_childs(child_elements)
