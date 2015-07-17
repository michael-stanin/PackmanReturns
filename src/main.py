import pygame
from pygame.locals import *


WIDTH   = 700
HEIGHT  = 500
CAPTION = "Packman Returns"

class Game:

    def __init__(self):
        self.status   = True
        self.size     = (WIDTH, HEIGHT)
        self.caption  = CAPTION

    def start(self):
        self._init_pygame()      

        while self.status:
            for event in pygame.event.get():
                self._on_event(event)

            self._on_loop()

            self._on_render()

        self._on_cleanup()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

    def _on_event(self, event):
        if event.type == pygame.QUIT:
            self.status = False

    def _on_loop(self):
        pass

    def _on_render(self):
        pass

    def _on_cleanup(self):
        pygame.quit()

game = Game()
game.start()
