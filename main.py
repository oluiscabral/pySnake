import pygame
import sys
from src.display import MainDisplay

pygame.init()
screen = pygame.display.set_mode([300, 300])
display = MainDisplay(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        display.K_LEFT()
    if key_input[pygame.K_UP]:
        display.K_UP()
    if key_input[pygame.K_RIGHT]:
        display.K_RIGHT()
    if key_input[pygame.K_DOWN]:
        display.K_DOWN()

    screen.fill([0, 0, 0])
    display.draw()
    pygame.display.flip()
