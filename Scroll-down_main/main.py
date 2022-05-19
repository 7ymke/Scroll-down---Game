import pygame
import button

#create display window
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
settings_img = pygame.image.load('source/textures/gui/settings_button.png').convert_alpha()
exit_img = pygame.image.load('source/textures/gui/exit_button.png').convert_alpha()
GUI_Image = pygame.image.load('source/textures/gui/GUI.png').convert_alpha()

#create button instances
settings_button = button.Button(20, 20, settings_img, 0.1)
exit_button = button.Button(220, 27, exit_img, 0.07)
gui_shown = 0
#game loop
run = True
while run:

    screen.fill((26, 173, 151))
    if gui_shown == 1:
        screen.blit(GUI_Image, (20, 15))
        if exit_button.draw(screen):
            run = False
    if settings_button.draw(screen):
        gui_shown = abs(int(gui_shown) - 1)
    

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    
pygame.quit()