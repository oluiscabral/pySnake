from pygame.surface import Surface
class GeneralConfig:
    def __init__(self, surface:Surface, target_fps: int):
        self.__surface = surface
        self.__target_fps = target_fps
    
    def get_surface(self) -> Surface:
        return self.__surface
    
    def get_target_fps(self) -> int:
        return self.__target_fps
    
