import pygame


class Display:
    def __init__(self, contents, active: bool):
        self.contents = contents
        self.__active = active

    def draw(self):
        if self.__active:
            for content in self.contents:
                content.draw()

    def K_UP(self):
        if self.__active:
            for content in self.contents:
                content.K_UP()

    def K_DOWN(self):
        if self.__active:
            for content in self.contents:
                content.K_DOWN()

    def K_LEFT(self):
        if self.__active:
            for content in self.contents:
                content.K_LEFT()

    def K_RIGHT(self):
        if self.__active:
            for content in self.contents:
                content.K_RIGHT()

    def K_SPACE(self):
        if self.__active:
            for content in self.contents:
                content.K_SPACE()

    def K_KP_ENTER(self):
        if self.__active:
            for content in self.contents:
                content.K_KP_ENTER()


class Content(Display):
    def __init__(self, screen: pygame.surface.Surface):
        self.__screen = screen
        super().__init__(None, True)

    def draw(self):
        pass

    def get_screen(self):
        return self.__screen

    def K_UP(self):
        pass

    def K_DOWN(self):
        pass

    def K_LEFT(self):
        pass

    def K_RIGHT(self):
        pass

    def K_SPACE(self):
        pass

    def K_KP_ENTER(self):
        pass


class LeftContent(Content):
    def __init__(self, screen: pygame.surface.Surface):
        super().__init__(screen)

    def draw(self):
        # light shade of the button
        pygame.draw.rect(self.get_screen(), (100, 100, 100), [0, 0, 100, 300])

    def K_UP(self):
        print('alooooooo')


class RightContent(Content):
    def __init__(self, screen: pygame.surface.Surface):
        super().__init__(screen)

    def draw(self):
        # light shade of the button
        pygame.draw.rect(self.get_screen(), (100, 100, 100),
                         [200, 0, 100, 300])


class MenuDisplay(Display):
    def __init__(self, active: bool, screen: pygame.surface.Surface):
        contents: list(Content) = [
            LeftContent(screen),
            RightContent(screen)
        ]
        super().__init__(contents, active)


class TopContent(Content):
    def __init__(self, screen: pygame.surface.Surface):
        super().__init__(screen)

    def draw(self):
        # light shade of the button
        pygame.draw.rect(self.get_screen(), (100, 100, 100), [50, 50, 140, 40])


class GameContent(Content):
    def __init__(self, screen: pygame.surface.Surface):
        super().__init__(screen)

    def draw(self):
        # light shade of the button
        pygame.draw.rect(self.get_screen(), (100, 100, 100), [50, 50, 20, 40])


class GameDisplay(Display):
    def __init__(self, active: bool, screen: pygame.surface.Surface):
        contents: list(Content) = [
            TopContent(screen),
            GameContent(screen)
        ]
        super().__init__(contents, active)


class MainDisplay(Display):
    def __init__(self, screen: pygame.surface.Surface):
        contents: list(Display) = [
            MenuDisplay(True, screen),
            GameDisplay(False, screen)
        ]
        super().__init__(contents, True)
