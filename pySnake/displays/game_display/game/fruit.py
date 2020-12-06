from pySnake.element import Element
import typing
import pygame
from pygame import Surface

from pySnake.colors import Colors
from pySnake.display import Display

class Fruit(Element):
    def __init__(self, surface: Surface, parent:Display, pos: typing.Tuple[int,int], size: typing.Tuple[int,int]):
        self.__color = Colors.blue_green
        super().__init__(surface, parent, pos, size)
    
    def draw(self, mouse_pos: typing.Tuple[int, int] = None):
        pygame.draw.rect(self.get_surface(), self.__color, [self.get_x(), self.get_y(), self.get_width(), self.get_height()])