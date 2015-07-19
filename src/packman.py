from block import *


RIGHT_ANGLE_DEGREES = 90
ZERO_POINT          = (0, 0)
ZERO                = 0
WIDTH               = 800
HEIGHT              = 640
PACKMAN_STEP        = 5
BLACK_COLOR         = (0, 0, 0)

class Packman(pygame.sprite.Sprite):

    def __init__(self, x, y, image=None):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pellets      = ZERO
        self.image_right  = self.image
        self.image_left   = pygame.transform.flip(self.image, True, False)
        self.image_up     = pygame.transform.rotate(self.image, RIGHT_ANGLE_DEGREES)
        self.image_down   = pygame.transform.rotate(self.image, -RIGHT_ANGLE_DEGREES)
        self.blocks       = None#pygame.sprite.Group()
        # Set speed vector
        self.change_x     = ZERO
        self.change_y     = ZERO

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        key = pygame.key.get_pressed()
        self.test_movement(key)

    def _change_direction(self, key):
        if key[pygame.K_LEFT]:
            self.image = self.image_left
        elif key[pygame.K_RIGHT]:
            self.image = self.image_right
        elif key[pygame.K_UP]:
            self.image = self.image_up
        elif key[pygame.K_DOWN]:
            self.image = self.image_down

    def _collide_with_blocks_x(self, key):
        # Did this update cause us to hit a wall?
        blocks_hit = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in blocks_hit:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if key[pygame.K_RIGHT]:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

    def _collide_with_blocks_y(self, key):
        # Check and see if we hit anything
        blocks_hit = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in blocks_hit:
 
            # Reset our position based on the top/bottom of the object.
            if key[pygame.K_DOWN]:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

    def test_movement(self, key):
        self._change_direction(key)

        # Move left/right
        self.rect.x += self.change_x

        self._collide_with_blocks_x(key)
 
        # Move up/down
        self.rect.y += self.change_y
 
        self._collide_with_blocks_y(key)