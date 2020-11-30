from pySnake.element.display import Display
from pySnake.element import Element
import typing

class MenuDisplay(Display):
    def __init__(self, active: bool):
        child_elements: typing.List[Element] = [
            
        ]
        super().__init__(child_elements, active)