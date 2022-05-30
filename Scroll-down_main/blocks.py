import pygame
from constants import BLOCKS, BLOCK_SIZE

class Block():
    def __init__(self,):
        pass
    def draw_block(self, surface, x, y, type, portaltype=''):
        
        
        surface.blit(type,(x, y))
