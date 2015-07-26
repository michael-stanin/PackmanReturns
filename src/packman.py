import gameobj


RIGHT_ANGLE_DEGREES = 90
ZERO_POINT          = (0, 0)
ZERO                = 0
PACKMAN_IMAGE_FILE  = "../resources/sprites/24x24packman.png"


class Packman(gameobj.GameObj):

    def __init__(self, x, y):
        super(Packman, self).__init__(x, y, PACKMAN_IMAGE_FILE)
        self.image_right       = self.image
        self.image_left        = gameobj.pygame.transform.flip(self.image, True, False)
        self.image_up          = gameobj.pygame.transform.rotate(self.image, RIGHT_ANGLE_DEGREES)
        self.image_down        = gameobj.pygame.transform.rotate(self.image, -RIGHT_ANGLE_DEGREES)
        self.blocks            = None
        self.pellets           = None
        self.pellets_collected = ZERO

        # Set speed vector
        self.change_x          = ZERO
        self.change_y          = ZERO

    @property
    def pos(self):
        return (self.rect.x, self.rect.y)
        
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        key = gameobj.pygame.key.get_pressed()
        self.move(key)

    def _change_direction(self, key):
        if key[gameobj.pygame.K_LEFT]:
            self.image = self.image_left
        elif key[gameobj.pygame.K_RIGHT]:
            self.image = self.image_right
        elif key[gameobj.pygame.K_UP]:
            self.image = self.image_up
        elif key[gameobj.pygame.K_DOWN]:
            self.image = self.image_down

    def _collide_with_pellets(self):
        pellets = gameobj.pygame.sprite.spritecollide(self, self.pellets, True)
        self.pellets_collected += len(pellets)

    def move(self, key):
        self._change_direction(key)

        # Move left/right
        self.rect.x += self.change_x

        self._collide_with_pellets()

        self._collide_with_blocks_x(key)
 
        # Move up/down
        self.rect.y += self.change_y

        self._collide_with_pellets()
        
        self._collide_with_blocks_y(key)