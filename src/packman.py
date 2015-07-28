import gameobj


RIGHT_ANGLE_DEGREES       = 90
ZERO_POINT                = (0, 0)
ZERO                      = 0
ANIMATION_FRAME_DEFAULT   = 1
PACKMAN_IMAGE_FILE        = "../resources/sprites/24x24packman2.png"
PACKMAN_SPRITES_FOLDER    = "../resources/sprites/"

class Packman(gameobj.GameObj):

    def __init__(self, x, y):
        super(Packman, self).__init__(x, y, PACKMAN_IMAGE_FILE)
        self._set_images()
        self.blocks            = None
        self.pellets           = None
        self.pellets_collected = ZERO

        self.animFrame         = ANIMATION_FRAME_DEFAULT

        # Set speed vector
        self.change_x          = ZERO
        self.change_y          = ZERO

    def _set_images(self):

        self.anim_pacmanL = {}
        self.anim_pacmanR = {}
        self.anim_pacmanU = {}
        self.anim_pacmanD = {}
        self.anim_pacmanS = {}
        self.anim_pacmanCurrent = {}
        
        for i in range(1, 9, 1):
            self.anim_pacmanR[i] = gameobj.pygame.image.load(PACKMAN_SPRITES_FOLDER + "packman-r " + str(i) + ".gif").convert_alpha()
            self.anim_pacmanL[i] = gameobj.pygame.transform.flip(self.anim_pacmanR[i], True, False)
            self.anim_pacmanU[i] = gameobj.pygame.transform.rotate(self.anim_pacmanR[i], RIGHT_ANGLE_DEGREES)
            self.anim_pacmanD[i] = gameobj.pygame.transform.rotate(self.anim_pacmanR[i], -RIGHT_ANGLE_DEGREES)
            self.anim_pacmanS[i] = gameobj.pygame.image.load(PACKMAN_SPRITES_FOLDER + "packman.gif").convert_alpha()

        # Initialize default one.
        self.anim_pacmanCurrent = self.anim_pacmanR

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
        # set the current frame array to match the direction pacman is facing
        if self.change_x > 0:
            self.anim_pacmanCurrent = self.anim_pacmanR
        elif self.change_x < 0:
            self.anim_pacmanCurrent = self.anim_pacmanL
        elif self.change_y > 0:
            self.anim_pacmanCurrent = self.anim_pacmanD
        elif self.change_y < 0:
            self.anim_pacmanCurrent = self.anim_pacmanU

        self.image = self.anim_pacmanCurrent[ self.animFrame ]
        
        if not self.change_x == 0 or not self.change_y == 0:
            # only Move mouth when pacman is moving
            self.animFrame += 1 
        
        if self.animFrame == 9:
            # wrap to beginning
            self.animFrame = 1

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