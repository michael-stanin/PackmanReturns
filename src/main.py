import pygame
from pygame.locals import *


WIDTH  = 700
HEIGHT = 500

class Game:

    def __init__(self):
        self.status   = True
        self.size     = (WIDTH, HEIGHT)
        self.caption  = "Packman Returns"

    def start(self):
        self._init_pygame()      

        while self.status:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

game = Game()
game.start()
