import pygame


class GameObj(pygame.sprite.Sprite):

    def __init__(self, x, y, image=None):
        super().__init__()
        if image:
            self.image             = pygame.image.load(image).convert_alpha()
            self.rect              = self.image.get_rect()
            self.rect.x            = x
            self.rect.y            = y