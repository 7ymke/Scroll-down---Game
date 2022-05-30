import pygame
import blocks
import button
from constants import BLOCK_WIDTH, starting_level_creator_x, starting_level_creator_y, BLOCK_HEIGHT, BLOCK_SIZE, BLOCK_SIZE, BLOCKS
level = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
['', '', '', '', '', '', '', '', '', ''], 
['', '', '', '', '', '', '', '', '', ''], 
['', '', '', '', '', '', '', '', '', ''], 
['', '', '', '', '', '', '', '', '', ''], 
['', '', '', '', '', '', '', '', '', ''], 
['', '', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', '', ''], 
['', '', '', '', '', '', '', '', '', ''], 
['', '', '', '', '', '', '', '', '', ''], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]




class Level_creator():
    

    def __init__(self, level) -> None:
        self.level = level

    def draw_level(self, surface):
        block1 = pygame.image.load(BLOCKS[0]).convert_alpha()   
        block2 = pygame.image.load(BLOCKS[1]).convert_alpha()
        block3 = pygame.image.load(BLOCKS[2]).convert_alpha()
        block = blocks.Block()
        for i in range(BLOCK_HEIGHT):
            for j in range(BLOCK_WIDTH):
                if self.level[i][j] != '':
                    if self.level[i][j] == 0:
                        type = block1
                    elif self.level[i][j] == 1:
                        type = block2
                    else:
                        type = block3

                    block.draw_block(surface, starting_level_creator_x + j * BLOCK_SIZE - j // 5, starting_level_creator_y + i * BLOCK_SIZE - i //5, type)
