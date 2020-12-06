import typing
import abc

from pygame import Surface
from pySnake.position import Position

class Element:
    
    def __init__(self, surface: Surface, parent: 'Element', pos: typing.Tuple[int,int], size: typing.Tuple[int,int]):
        self.__position = self.__init_pos(parent, pos)
        self.__width, self.__height = size
        self.__surface = surface
    
    def __init_pos(self, parent: 'Element', pos: typing.Tuple[int, int]):
        ret = Position(pos)
        if parent != None and parent.get_pos() != None:
            ret.update(parent.get_pos().get())
        return ret
    
    @abc.abstractmethod
    def action(self, representation: str):
        pass
    
    def get_pos(self) -> Position:
        return self.__position
    
    def get_x(self) -> int:
        return self.__position.get_x()
    
    def get_y(self) -> int:
        return self.__position.get_y()
    
    def get_size(self) -> typing.Tuple[int,int]:
        return self.__width, self.__height
    
    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height
    
    def get_surface(self) -> Surface:
        return self.__surface
    
    def get_x_coverage(self):
        return self.get_x() + self.__width
    
    def get_y_coverage(self):
        return self.get_y() + self.__height
    
    def get_parent(self) -> 'Element':
        return self.__parent
    
    @abc.abstractmethod
    def draw(self, mouse_pos: typing.Tuple[int, int] = None):
        pass
    
    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def K_UP(self):
        pass

    @abc.abstractmethod
    def K_DOWN(self):
        pass

    @abc.abstractmethod
    def K_LEFT(self):
        pass

    @abc.abstractmethod
    def K_RIGHT(self):
        pass

    @abc.abstractmethod
    def K_SPACE(self):
        pass

    @abc.abstractmethod
    def K_KP_ENTER(self):
        pass

    @abc.abstractmethod
    def L_CLICK(self, mouse_x: int, mouse_y: int):
        pass

    @abc.abstractmethod
    def M_CLICK(self, mouse_x: int, mouse_y: int):
        pass

    @abc.abstractmethod
    def R_CLICK(self, mouse_x: int, mouse_y: int):
        pass
    
