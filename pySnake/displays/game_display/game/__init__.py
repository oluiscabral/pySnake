from pySnake.element import Element
from pySnake.display import Display
import typing
from pySnake.displays.game_display.game.fruit import Fruit
from pygame import Surface
import pygame
from pySnake.displays.game_display.game.utils import GameUtils
from pySnake.displays.game_display.game.snake import Snake
from pySnake.config import GeneralConfig
import time
import timeit
from pySnake.displays.game_display.game.grid import Grid

class SnakeGame(Display, GameUtils):
    def __init__(self, config: GeneralConfig, parent: Display, pos: typing.Tuple[int,int], size: typing.Tuple[int,int]):
        super().__init__(config, parent, pos, size, True)
        self.__grid_unit = 10
        
        self.__grid = Grid(config, parent, pos, size, self.__grid_unit)
        
        self.add_childs(self.__init_elements())
        
        self.add_childs([self.__grid])
        self.__transit_frame = self.__get_transit_frame(self.get_config().get_target_fps(), 2)
        self.__frame: int = 0
    
    def draw(self, mouse_pos:typing.Tuple[int, int]=None):
        self.__draw_self()
        super().draw(mouse_pos)
    
    def update(self):
        if self.__frame == self.__transit_frame:
            self.__frame = 0
            super().update()
        self.__frame += 1
    
    
    def __get_transit_frame(self, general_fps, target_fps):
        return (general_fps // target_fps)*2
    
    def __draw_self(self):
        pygame.draw.rect(self.get_surface(), (100,100,100), [self.get_x(), self.get_y(), self.get_width(), self.get_height()])
    
    def __init_elements(self) -> typing.List[Element]:
        size_unit = 10
        return [
            Fruit(self.get_surface(), self, self.get_random_pos(self.get_width()-size_unit, self.get_height()-size_unit), [size_unit, size_unit]),
            Snake(self.get_surface(), self, self.get_random_pos(self.get_width()-size_unit, self.get_height()-size_unit), [size_unit, size_unit])
            ]