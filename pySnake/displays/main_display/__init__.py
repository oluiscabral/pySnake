import typing
from pySnake.display import Display
from pySnake.element import Element
from pySnake.displays.game_display import GameDisplay
from pySnake.displays.menu_display import MenuDisplay
from pygame import Surface
from pySnake.config import GeneralConfig

class MainDisplay(Display):
    def __init__(self, config: GeneralConfig):
        super().__init__(config, None, (0,0), config.get_surface().get_size(), True)
        child_elements: typing.List[Element] = [
            GameDisplay(config, self, True)
        ]
        self.add_childs(child_elements)
    
    def update(self, mouse_pos: typing.Tuple[int, int] = None):
        super().draw(mouse_pos)
        super().update()