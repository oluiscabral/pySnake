from pySnake.element import Element
import typing
from pySnake.config import GeneralConfig

class Display(Element):
    def __init__(self, config: GeneralConfig, parent: 'Display', pos: typing.Tuple[int,int], size: typing.Tuple[int,int], active: bool = False):
        super().__init__(config.get_surface(), parent, pos, size)
        self.__child_elements = []
        self.__active = active
        self.__config = config
    
    def get_config(self) -> GeneralConfig:
        return self.__config
    
    def add_childs(self, child_elements: typing.List[Element]):
        self.__child_elements.extend(child_elements)
    
    def action(self, representation:str):
        self.__spread_action(representation)
    
    def __spread_action(self, representation):
        for element in self.__child_elements:
            element.action(representation)
    
    def __set_active(self, value: bool = None):
        if value is None:
            self.__active = not self.__active
        else:
            self.__active = value
    
    def is_active(self) -> bool:
        return self.__active
    
    def draw(self, mouse_pos: typing.Tuple[int, int] = None):
        if self.__active:
            for element in self.__child_elements:
                element.draw(mouse_pos)
    
    def update(self):
        if self.__active:
            for element in self.__child_elements:
                    element.update()

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