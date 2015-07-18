import pygame
from pygame.locals import *


RIGHT_ANGLE_DEGREES = 90
ZERO_POINT          = (0, 0)
ZERO                = 0
WIDTH               = 960
HEIGHT              = 640
PACKMAN_STEP        = 8

class Packman(pygame.sprite.Sprite):

    def __init__(self, image=None, *groups):
        super(Packman, self).__init__(*groups)
        self.pellets      = ZERO
        self.image        = pygame.image.load(image)
        self.image_right  = self.image
        self.image_left   = pygame.transform.flip(self.image, True, False)
        self.image_up     = pygame.transform.rotate(self.image, RIGHT_ANGLE_DEGREES)
        self.image_down   = pygame.transform.rotate(self.image, -RIGHT_ANGLE_DEGREES)
        self.rect         = pygame.rect.Rect(ZERO_POINT, self.image.get_size())

    def update(self):
        key = pygame.key.get_pressed()
        # Actual movement.
        self._movement(key)

        # Restrictions
        self._restrictions()

    def _restrictions(self):
        self._window_restrictions()

    def _window_restrictions(self):
        if self.rect.y + PACKMAN_STEP >= HEIGHT:
            self.rect.y = HEIGHT - PACKMAN_STEP - self.image.get_size()[1]
        elif self.rect.y <= ZERO:
            self.rect.y = ZERO
        if self.rect.x + PACKMAN_STEP >= WIDTH:
            self.rect.x = WIDTH - PACKMAN_STEP - self.image.get_size()[0] 
        if self.rect.x <= ZERO:
            self.rect.x = ZERO

    def _movement(self, key):
        if key[pygame.K_LEFT]:
            self.rect.x -= PACKMAN_STEP
            self.image = self.image_left
        elif key[pygame.K_RIGHT]:
            self.rect.x += PACKMAN_STEP
            self.image = self.image_right
        elif key[pygame.K_UP]:
            self.rect.y -= PACKMAN_STEP
            self.image = self.image_up
        elif key[pygame.K_DOWN]:
            self.rect.y += PACKMAN_STEP
            self.image = self.image_down
 
    def collide(self, other):
        pass
