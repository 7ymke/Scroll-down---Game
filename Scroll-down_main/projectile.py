from tarfile import BLOCKSIZE
import pygame 
from constants import starting_level_creator_x, starting_level_creator_y
import math


class Projectile:
    def __init__(self):
        pass

    
    def launch(launched):
        if launched[0]:
            return launched
        elif pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[pygame.K_SPACE]:
            return (True, math.floor(pygame.mouse.get_pos()[1] - 25.5))
        else:
            return (False, 0)
    
    def draw(surface, posx, posy, img):
        surface.blit(img,(posx, posy))
    
    def get_pos(posx, posy):
        return (math.floor((posx - 705 + 25.5)/ 51), math.floor((posy - 285 + 25.5)/ 51 + 2.5))
