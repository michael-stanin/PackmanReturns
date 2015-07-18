import pygame

from packman import *


CAPTION            = "Packman Returns"
BACKGROUND_IMAGE   = "../resources/backgrounds/2.jpg"
PACKMAN_IMAGE_FILE = "../resources/sprites/24x24packman.png"

class Game:

    def __init__(self):
        self.status      = True
        self.size        = (WIDTH, HEIGHT)
        self.caption     = CAPTION
        self.dirty_rects = []

    def start(self):
        self._init_pygame()

        self.background = pygame.image.load(BACKGROUND_IMAGE)
        self.dirty_rects.append(self.background.get_rect())

        self._load_sprites()

        clock = pygame.time.Clock()        

        while self.status:
            # Limit frame speed to 60 FPS.
            time_passed = clock.tick(60)

            for event in pygame.event.get():
                self._on_event(event)

            self._on_loop()

            self._on_render()

        self._on_cleanup()

    def _init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

    def _on_event(self, event):
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and
            event.key == K_ESCAPE):
            self.status = False
        

    def _on_loop(self):
        self.screen.blit(self.background, ZERO_POINT)

        self.packman_sprites.update()
        self.packman_sprites.draw(self.screen)

        pygame.display.flip()
        pygame.display.update(self.dirty_rects)


    def _on_render(self):
        pass

    def _on_cleanup(self):
        pygame.quit()

    def _load_sprites(self):
        self._load_packman()

        self._load_ghosts()

        self._load_walls()

        self._load_pellets()

    def _load_packman(self):
        self.packman = Packman(PACKMAN_IMAGE_FILE, pygame.sprite.Group())
        self.packman_sprites = pygame.sprite.RenderPlain(self.packman)
        self.dirty_rects.append(self.packman.image.get_rect())
        
    def _load_ghosts(self):
        pass

    def _load_walls(self):
        pass

    def _load_pellets(self):
        pass

game = Game()
game.start()
