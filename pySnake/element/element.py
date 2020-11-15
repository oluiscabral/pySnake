import typing
import abc
import pygame


class Element:
    @abc.abstractmethod
    def draw(self, mouse_pos: typing.Tuple[int, int] = None):
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
