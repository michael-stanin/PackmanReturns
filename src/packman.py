from pygame.locals import sprite.Sprite as MichaelSprite


RIGHT_ANGLE_DEGREES = 90
ZERO_POINT          = (0, 0)
ZERO                = 0
WIDTH               = 700
HEIGHT              = 500
PACKMAN_STEP        = 8

class Packman(MichaelSprite):

    def __init__(self, image=None, *args, **kwargs):
        self.pellets      = ZERO
        self.image        = image
        self.image_right  = self.image
        self.image_left   = pygame.transform.flip(self.image, True, False)
        self.image_up     = pygame.transform.rotate(self.image, RIGHT_ANGLE_DEGREES
        self.image_down   = pygame.transform.rotate(self.image, -RIGHT_ANGLE_DEGREES)
        self.rect         = pygame.rect.Rect(ZERO_POINT, self.image.get_size())

    def update(self):
        # Restrictions.
        self._restrictions()
        
        key = pygame.key.get_pressed()
        # Actual movement.
        self._movement(key)

    def _restrictions(self):
        self._window_restrictions()

    def _window_restrictions(self):
        if self.rect.y >= HEIGHT:
            self.rect.y = HEIGHT
        elif self.rect.y <= ZERO:
            self.rect.y = ZERO
        if self.rect.x >= WIDTH:
            self.rect.x = WIDTH
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
