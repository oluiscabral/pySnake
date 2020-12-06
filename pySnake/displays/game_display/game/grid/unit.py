from pySnake.element import Element
from pygame import Surface
import typing
import pygame
from pySnake.colors import Colors

class Unit(Element):
    def __init__(self, surface: Surface, parent: 'Element', pos: typing.Tuple[int,int], size: typing.Tuple[int,int]):
        super().__init__(surface, parent, pos, size)
        self.__color = Colors.white
        self.__dellocation = 2
    
    def draw(self, mouse_pos: typing.Tuple[int,int]=None):
        pygame.draw.rect(self.get_surface(), self.__color, [self.get_x()+self.__dellocation, self.get_y()+self.__dellocation, self.get_width()-self.__dellocation, self.get_height()-self.__dellocation])
        