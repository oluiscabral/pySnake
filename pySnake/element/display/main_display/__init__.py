import typing
from ...display import Display
from ....element import Element

from .game_display import GameDisplay
from .menu_display import MenuDisplay

class MainDisplay(Display):
    def __init__(self):
        child_elements: typing.List[Element] = [
            MenuDisplay(True),
            GameDisplay(False)
        ]
        super().__init__(child_elements, True)
