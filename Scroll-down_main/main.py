import pygame
import button
import level_code
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS

#create display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
level = level_code.level
level_creator = level_code.Level_creator(level)


pygame.display.set_caption('Button Demo')

#load button images
settings_img = pygame.image.load('Scroll-down_main/source/textures/gui/settings_button.png').convert_alpha()
exit_img = pygame.image.load('Scroll-down_main/source/textures/gui/exit_button.png').convert_alpha()
GUI_Image = pygame.image.load('Scroll-down_main/source/textures/gui/GUI.png').convert_alpha()
#icon managment

icon_image = pygame.image.load('Scroll-down_main/source/textures/gui/icon.jpg').convert_alpha()
pygame.display.set_icon(icon_image)
#create button instances
settings_button = button.Button(20, 20, settings_img, 0.1)
exit_button = button.Button(220, 27, exit_img, 0.07)
portaltype = 1
gui_shown = 0
#game loop
run = True
num = 1
clock = pygame.time.Clock()
while run:
    
    if num % 5 == 0:
        portaltype += 1
    if portaltype == 18:
        portaltype = 1
    clock.tick(MAX_FPS)
    screen.fill((20 * num % 5, 173, 151))
    level_creator.draw_level(screen, str(portaltype))
    if gui_shown == 1:
        screen.blit(GUI_Image, (20, 15))
        if exit_button.draw(screen):
            run = False
    if settings_button.draw(screen):
        gui_shown = abs(int(gui_shown) - 1)
    num += 1
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    
pygame.quit()