import pygame
import random

from pygame.locals import *
from block   import Block
from packman import Packman
from blinky  import Blinky
from layout  import Layout
from pellet  import Pellet
from colors  import BLACK

CAPTION                  = "Packman Returns"
BACKGROUND_IMAGE_FILE    = "../resources/backgrounds/2.jpg"

LEVEL_ONE_GRID_FOLDER    = "../resources/levels/1/"

BLOCKS_LAYOUT_FILE       = "blocks_layout.txt"
PELLETS_LAYOUT_FILE      = "pellets_layout.txt"

PACKMAN_STEP             = 5

WIDTH                    = 800
HEIGHT                   = 640


class Game:

    def __init__(self):
        self.status          = True
        self.size            = (WIDTH, HEIGHT)
        self.caption         = CAPTION
        self.dirty_rects     = pygame.sprite.Group()
        self.limit_cells     = []
        self.block_locations = []

    def start(self):
        self.layout = Layout(LEVEL_ONE_GRID_FOLDER)

        self._init_pygame()

        self._load_sprites()

        self._fill_limit_cells()

        clock = pygame.time.Clock()        

        while self.status:
            # Limit frame speed to 60 FPS.
            time_passed = clock.tick(60)

            # Handle key events.
            for event in pygame.event.get():
                self._on_event(event)

            self._on_render()

            # Update all of the needed sprites
            self._on_loop()


        # Close app.
        self._on_cleanup()

    def _init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

    def _on_event(self, event):
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and
            event.key == K_ESCAPE):
            self.status = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.packman.changespeed(-PACKMAN_STEP, 0)
            elif event.key == pygame.K_RIGHT:
                self.packman.changespeed(PACKMAN_STEP, 0)
            elif event.key == pygame.K_UP:
                self.packman.changespeed(0, -PACKMAN_STEP)
            elif event.key == pygame.K_DOWN:
                self.packman.changespeed(0, PACKMAN_STEP)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.packman.changespeed(PACKMAN_STEP, 0)
            elif event.key == pygame.K_RIGHT:
                self.packman.changespeed(-PACKMAN_STEP, 0)
            elif event.key == pygame.K_UP:
                self.packman.changespeed(0, PACKMAN_STEP)
            elif event.key == pygame.K_DOWN:
                self.packman.changespeed(0, -PACKMAN_STEP)
        

    def _on_loop(self):
        self.screen.fill(BLACK)

        self.dirty_rects.update()
        self.dirty_rects.draw(self.screen)

        pygame.sprite.spritecollide(self.packman, self.ghosts, False)

        pygame.display.flip()

    def _on_render(self):
        pos = self.packman.pos
        for ghost in self.ghosts:
            ghost.packman_pos = pos
            ghost.draw(self.screen)

    def _on_cleanup(self):
        pygame.quit()

    def _load_sprites(self):

        self._load_walls()

        self._load_pellets()

        self._load_packman()

        self._load_ghosts()

    def _load_packman(self):
        self.packman = Packman(400, 320)
        self.packman.blocks = self.blocks
        self.packman.pellets = self.pellets
        self.dirty_rects.add(self.packman)
        
    def _load_ghosts(self):
        self.ghosts = pygame.sprite.Group()
        for x in [340, 370, 400, 430]:
            ghost = Blinky(x, 290, self.packman.pos)
            ghost.blocks = self.blocks

            self.ghosts.add(ghost)
            self.dirty_rects.add(ghost)



    def _load_walls(self):
        self.blocks = pygame.sprite.Group()
        blocks_layout = self.layout.read_layout(BLOCKS_LAYOUT_FILE)

        for line in blocks_layout:
            block = Block(int(line[0]),
                          int(line[1]),
                          int(line[2]),
                          int(line[3]))

            self.limit_cells.append((block.rect.topleft, block.rect.bottomright))

            self.blocks.add(block)
            self.dirty_rects.add(block)

    def _load_pellets(self):
        self.pellets = pygame.sprite.Group()
        pellets_layout = self.layout.read_layout(PELLETS_LAYOUT_FILE)

        for line in pellets_layout:
            pellet = Pellet(int(line[0]),
                            int(line[1]),
                            int(line[2]))

            self.pellets.add(pellet)
            self.dirty_rects.add(pellet)

    def _fill_limit_cells(self):
        for pair in self.limit_cells:
            self._fill_limit_cell(pair)

    def _fill_limit_cell(self, pair):
        #include the border cases
        for x in range(pair[0][0], pair[1][0] + 1):
            for y in range(pair[0][1], pair[1][1] + 1): 
                self.block_locations.append((x,y))

game = Game()
game.start()
