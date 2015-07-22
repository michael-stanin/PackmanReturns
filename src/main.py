import pygame
import random

from packman import *
from layout import *
from pellet import *

CAPTION                  = "Packman Returns"
BACKGROUND_IMAGE_FILE    = "../resources/backgrounds/2.jpg"
PACKMAN_IMAGE_FILE       = "../resources/sprites/24x24packman.png"
LEVEL_ONE_GRID_FILE      = "../resources/levels/1/"
PELLET_IMAGE_FILE        = "../resources/sprites/pellet.png"
BLOCK_IMAGE_FILE         = "../resources/sprites/wall.png"



class Game:

    def __init__(self):
        self.status      = True
        self.size        = (WIDTH, HEIGHT)
        self.caption     = CAPTION
        self.score       = ZERO
        self.dirty_rects = pygame.sprite.Group()

    def start(self):
        self.layout = Layout(LEVEL_ONE_GRID_FILE)

        self._init_pygame()

        self._load_sprites()

        clock = pygame.time.Clock()        

        while self.status:
            # Limit frame speed to 60 FPS.
            time_passed = clock.tick(60)

            # Handle key events.
            for event in pygame.event.get():
                self._on_event(event)

            # Update all of the needed sprites
            self._on_loop()

            self._on_render()

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
        self.screen.fill(BLACK_COLOR)

        self.dirty_rects.update()
        self.dirty_rects.draw(self.screen)

        pygame.display.flip()

    def _track_score(self, pellets):
        for pellet in pellets:
            self.score += 1

    def _on_render(self):
        pass

    def _on_cleanup(self):
        pygame.quit()

    def _load_sprites(self):

        self._load_ghosts()

        self._load_walls()

        self._load_pellets()

        self._load_packman()

    def _load_packman(self):
        self.packman = Packman(400, 320, PACKMAN_IMAGE_FILE)
        self.packman.blocks = self.blocks
        self.packman.pellets = self.pellets
        self.dirty_rects.add(self.packman)
        
    def _load_ghosts(self):
        pass

    def _load_walls(self):
        self.blocks = pygame.sprite.Group()
        blocks_layout = self.layout.read_layout(BLOCKS_LAYOUT_FILE)

        for line in blocks_layout:
            block = Block(int(line[0]),
                          int(line[1]),
                          int(line[2]),
                          int(line[3]))
            self.blocks.add(block)
            self.dirty_rects.add(block)


    def _load_pellets(self):
        self.pellets = pygame.sprite.Group()
        pellets_layout = self.layout.read_layout(PELLETS_LAYOUT_FILE)

        for line in pellets_layout:
            pellet = Pellet(int(line[0]),
                            int(line[1]),
                            int(line[2]), self.screen)

            self.pellets.add(pellet)
            self.dirty_rects.add(pellet)



game = Game()
game.start()
