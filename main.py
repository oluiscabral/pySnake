import pygame
import sys
from src.display import MainDisplay

pygame.init()
screen = pygame.display.set_mode([300, 300])
display = MainDisplay(screen)
mouse = {}
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
    if key_input[pygame.K_SPACE]:
        display.K_SPACE()
    if key_input[pygame.K_KP_ENTER]:
        display.K_KP_ENTER()

    mouse['x'], mouse['y'] = pygame.mouse.get_pos()
    mouse['L_CLICK'], mouse['M_CLICK'], mouse['R_CLICK'] = pygame.mouse.get_pressed(
        num_buttons=3)

    if mouse['L_CLICK']:
        display.L_CLICK(mouse['x'], mouse['y'])
    if mouse['M_CLICK']:
        display.M_CLICK(mouse['x'], mouse['y'])
    if mouse['R_CLICK']:
        display.R_CLICK(mouse['x'], mouse['y'])

    screen.fill([0, 0, 0])
    display.draw()
    pygame.display.flip()
