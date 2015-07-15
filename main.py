import pygame
from pygame.locals import *


class Game:

    def __init__(self):
        self.status = True

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))

        while self.status:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

game = Game()
game.start()
