from turtle import position
import pygame
import button
import level_code
import projectile
import math
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, starting_level_creator_x

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
direction = 180
#Projectile images
laser = pygame.image.load('Scroll-down_main/source/textures/Projectiles/Laser.png').convert_alpha()
laser = pygame.transform.rotate(laser, direction)

mirrors_used = []
#create button instances
settings_button = button.Button(20, 20, settings_img, 0.1)
exit_button = button.Button(220, 27, exit_img, 0.07)
portaltype = 1
gui_shown = 0
prox = 510 + starting_level_creator_x
proy = 540
test = 0

#game loop
launched = (False, 0)
run = True
num = 1
clock = pygame.time.Clock()
while run:
    screen.fill((20 * num % 5, 173, 151))
    level_creator.draw_level(screen, str(portaltype))
    
    if num > 120:
        launched = projectile.Projectile.launch(launched)
    if launched[0]:
        projectile.Projectile.draw(screen, prox, proy, laser)
        if test == 0:
            prox = 510 + starting_level_creator_x
            proy = launched[1]
            test = 1
        else:
            prox += math.cos(math.radians((direction + 1080) % 360))
            if direction == 180:
                proy += 0
            elif direction == 90:
                proy += 1
            elif direction == 270: 
                proy -= 1

    
    if abs(projectile.Projectile.get_pos(prox, proy)[1]) < 15:
        if abs(projectile.Projectile.get_pos(prox, proy)[0]) < 10:
            touching_block = level_code.level[abs(math.floor(projectile.Projectile.get_pos(prox, proy)[1]))][abs(math.floor(projectile.Projectile.get_pos(prox, proy)[0]))]
            if not touching_block == '' and touching_block[0] == 0:
                launched = (False, 0)
                prox = 510 + starting_level_creator_x
                proy = 540
                test = 0
                direction = 180
            elif projectile.Projectile.get_pos(prox, proy)[0] < 0 or projectile.Projectile.get_pos(prox, proy)[1] < 0 or projectile.Projectile.get_pos(prox, proy)[1] > 15:
                launched = (False, 0)
                prox = 510 + starting_level_creator_x
                proy = 540
                test = 0
                direction = 180
            elif not touching_block == '' and touching_block[0] == 1 and (projectile.Projectile.get_pos(prox, proy)) not in mirrors_used:
                mirrors_used.append(projectile.Projectile.get_pos(prox, proy))
                prox += math.cos(math.radians((direction + 1080) % 360)) * 51
                if direction == 180:
                    proy += 0
                elif direction == 90:
                    proy += 51
                elif direction == 270: 
                    proy -= 51
                direction += direction - 90 + touching_block[1]
                laser = pygame.transform.rotate(laser, direction)
                

                print(mirrors_used)
                
    if num % 5 == 0:
        portaltype += 1
    if portaltype == 18:
        portaltype = 1
    clock.tick(MAX_FPS)
    
    
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