import os
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
WHITE = (255,255,255)
MAX_FPS=60

GUI_BUTTON_SIZES = (50, 50)

BLOCKS = [os.path.join("Scroll-down_main", "source", 'textures', 'blocks', "block.png"), os.path.join("Scroll-down_main", "source", 'textures', 'blocks', "mirror.png"), 'Scroll-down_main/source/textures/blocks/portals/portal_']
BLOCK_SIZE = 51
BLOCK_WIDTH, BLOCK_HEIGHT = 10,15
starting_level_creator_x = (SCREEN_WIDTH-BLOCK_SIZE * BLOCK_WIDTH)/2
starting_level_creator_y = (SCREEN_HEIGHT-BLOCK_SIZE * BLOCK_HEIGHT)/2
