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
direction = 0
#Projectile images
laser_img = pygame.image.load('Scroll-down_main/source/textures/Projectiles/Laser.png').convert_alpha()
laser = pygame.transform.rotate(laser_img, direction)
portaltype = 1
gui_shown = 0
prox = 510 + starting_level_creator_x
proy = 540
test = 0
display_x = 0
display_y = 0
num = 1 
mirrors_used = []
launched = (False, 0)
#create button instances

settings_button = button.Button(20, 20, settings_img, 0.1)
exit_button = button.Button(220, 27, exit_img, 0.07)

#game loop

run = True

clock = pygame.time.Clock()
while run:
    screen.fill((20 * num % 5, 173, 151))
    
    
    if num > 120:
        launched = projectile.Projectile.launch(launched)
    if launched[0]:
        projectile.Projectile.draw(screen, prox + display_x, proy + display_y, laser)
        if test == 0:
            prox = 510 + starting_level_creator_x
            proy = launched[1]
            test = 1
        else:
            prox += math.cos(math.radians((direction + 1260) % 360))
            if direction == 0:
                proy += 0
            elif direction == 90:
                proy += 1
            elif direction == 270: 
                proy -= 1

    
    if abs(projectile.Projectile.get_pos(prox, proy)[1]) < 15:
        if abs(projectile.Projectile.get_pos(prox, proy)[0]) < 10:
            touching_block = level_code.level[abs(math.floor(projectile.Projectile.get_pos(prox, proy)[1]))][abs(math.floor(projectile.Projectile.get_pos(prox, proy)[0]))]
            if not touching_block == '' and touching_block[0] == 0:
                laser = pygame.transform.rotate(laser_img, direction)
                portaltype = 1
                prox = 510 + starting_level_creator_x
                proy = 540
                test = 0
                display_x = 0
                display_y = 0
                num = 1 
                mirrors_used = []
                launched = (False, 0)
                direction = 0
            elif projectile.Projectile.get_pos(prox, proy)[0] < 0 or projectile.Projectile.get_pos(prox, proy)[1] < 0 or projectile.Projectile.get_pos(prox, proy)[1] > 15:
                laser = pygame.transform.rotate(laser_img, direction)
                portaltype = 1
                prox = 510 + starting_level_creator_x
                proy = 540
                test = 0
                display_x = 0
                display_y = 0
                num = 1 
                mirrors_used = []
                launched = (False, 0)
                direction = 0
            elif not touching_block == '' and touching_block[0] == 1 and (projectile.Projectile.get_pos(prox, proy)) not in mirrors_used:
                mirrors_used.append(projectile.Projectile.get_pos(prox, proy))
                display_x += math.cos(math.radians((direction + 1260) % 360)) * 25.5
                if touching_block[1] == 0:
                    if direction == 0:
                        direction = 270
                        display_y = 25.5
                        display_x = -25.5
                    elif direction == 90:
                        direction = 180
                        display_y = -25.5
                        display_y = -25.5
                elif touching_block[1] == 90:
                    if direction == 180:
                        direction = 270
                        display_y = -25.5
                        display_x = -25.5
                    elif direction == 90:
                        display_y = 25.5
                        display_x = 0
                        direction = 0
                elif touching_block[1] == 180:
                    if direction == 270:
                        direction = 0
                        display_y = -25.5
                        display_x = -25.5
                    elif direction == 180:
                        direction = 90
                        display_y = 25.5
                        display_x = 25.5
                elif touching_block[1] == 270:
                    if direction == 0:
                        direction = 90
                        display_y = -25.5
                        display_x = -25.5
                    elif direction == 90:
                        display_y = 25.5
                        display_x = 25.5
                        direction = 180
                laser = pygame.transform.rotate(laser_img, direction)

                laser = pygame.transform.rotate(laser_img, direction)
        
            

            

    level_creator.draw_level(screen, str(portaltype))            
    direction = (direction + 360) % 360            
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