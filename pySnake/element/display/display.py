import typing
from element import Element


class Display(Element):
    def __init__(self, child_elements: typing.List[Element], active: bool):
        self.__child_elements = child_elements
        self.__active = active

    def draw(self, mouse_pos: typing.Tuple[int, int] = None):
        if self.__active:
            for element in self.__child_elements:
                element.draw(mouse_pos)

    def K_UP(self):
        if self.__active:
            for element in self.__child_elements:
                element.K_UP()

    def K_DOWN(self):
        if self.__active:
            for element in self.__child_elements:
                element.K_DOWN()

    def K_LEFT(self):
        if self.__active:
            for element in self.__child_elements:
                element.K_LEFT()

    def K_RIGHT(self):
        if self.__active:
            for element in self.__child_elements:
                element.K_RIGHT()

    def K_SPACE(self):
        if self.__active:
            for element in self.__child_elements:
                element.K_SPACE()

    def K_KP_ENTER(self):
        if self.__active:
            for element in self.__child_elements:
                element.K_KP_ENTER()

    def L_CLICK(self, mouse_x: int, mouse_y: int):
        if self.__active:
            for element in self.__child_elements:
                element.L_CLICK(mouse_x, mouse_y)

    def M_CLICK(self, mouse_x: int, mouse_y: int):
        if self.__active:
            for element in self.__child_elements:
                element.M_CLICK(mouse_x, mouse_y)

    def R_CLICK(self, mouse_x: int, mouse_y: int):
        if self.__active:
            for element in self.__child_elements:
                element.M_CLICK(mouse_x, mouse_y)
