import pygame
from constants import BLOCKS

class Block():
    def __init__(self,  type, portaltype=''):
        block_type = 'source/textures/blocks/' + BLOCKS[type] + '.png'
        block_type = pygame.image.load(str(block_type)).convert_alpha()
        self.type = pygame.transform.scale(block_type, (51.2, 51.2))
        self.portaltype=portaltype
    def draw_block(self, surface, x, y):
        surface.blit(self.type,(x, y))
