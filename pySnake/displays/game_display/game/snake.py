from pySnake.element import Element
import typing
import pygame
from pygame import Surface
from pySnake.display import Display
from pySnake.colors import Colors

class Snake(Element):
    def __init__(self, surface: Surface, parent:Display, pos: typing.Tuple[int,int], size: typing.Tuple[int,int]):
        super().__init__(surface, parent, pos, size)
        self.__color = Colors.yellow
        self.__speed = self.get_size()[0]
        self.__pos = self.get_pos()
    
    def draw(self, mouse_pos: typing.Tuple[int, int] = None):
        pygame.draw.rect(self.get_surface(), self.__color, [self.get_x(), self.get_y(), self.get_width(), self.get_height()])
    
    def update(self):
        self.__pos.update_x(self.__speed)