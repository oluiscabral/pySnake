import typing

class Position:
    def __init__(self, pos: typing.Tuple[int,int]):
        self.__x, self.__y = pos
    
    def get(self) -> typing.Tuple[int,int]:
        return (self.__x, self.__y)
    
    def set(self, pos: typing.Tuple[int, int]):
        self.__x, self.__y = pos
    
    def update(self, values: typing.Tuple[int, int]):
        self.__x += values[0]
        self.__y += values[1]
    
    def get_x(self) -> int:
        return self.__x
    
    def get_y(self) -> int:
        return self.__y
    
    def set_x(self, value:int):
        self.__x = value
    
    def set_y(self, value:int):
        self.__y = value
        
    def update_x(self, value: int):
        self.__x += value
    
    def update_y(self, value: int):
        self.__y += value