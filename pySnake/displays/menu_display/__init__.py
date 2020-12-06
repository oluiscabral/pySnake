from pySnake.element import Element
import typing
from pySnake.display import Display
from pygame import Surface

class MenuDisplay(Display):
    def __init__(self, surface: Surface, active: bool):
        child_elements: typing.List[Element] = [
            
        ]
        super().__init__(surface, child_elements, active)