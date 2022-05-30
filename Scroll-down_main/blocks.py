import pygame
from constants import  BLOCK_SIZE

class Block():
    def __init__(self,):
        pass
    def draw_block(self, surface, x, y, type, angle=0):
        type = pygame.transform.rotate(type, angle)
        
        surface.blit(type,(x, y))
