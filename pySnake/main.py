import pygame
import sys
from pySnake.displays.main_display import MainDisplay
import time
from pySnake.config import GeneralConfig


pygame.init()
target_fps = 60
screen = pygame.display.set_mode([500, 500])
config = GeneralConfig(screen, target_fps)
display = MainDisplay(config)
mouse = {}

target_fps = config.get_target_fps()
prev_time = time.time()
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

    mouse['pos'] = pygame.mouse.get_pos()
    mouse['L_CLICK'], mouse['M_CLICK'], mouse['R_CLICK'] = pygame.mouse.get_pressed(
        num_buttons=3)

    if mouse['L_CLICK']:
        display.L_CLICK(mouse['pos'][0], mouse['pos'][1])
    if mouse['M_CLICK']:
        display.M_CLICK(mouse['pos'][0], mouse['pos'][1])
    if mouse['R_CLICK']:
        display.R_CLICK(mouse['pos'][0], mouse['pos'][1])
    
    curr_time = time.time()
    diff = curr_time - prev_time
    delay = max(1.0/target_fps - diff, 0)
    time.sleep(delay)
    fps = 1.0/(delay + diff)
    prev_time = curr_time
    
    screen.fill([0, 0, 0])
    display.update(mouse['pos'])
    pygame.display.flip()
