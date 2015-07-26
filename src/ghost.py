import gameobj


ZERO                = 0
GHOST_FILE = "../resources/sprites/bad_guy.png"

class Ghost(gameobj.GameObj):

    def __init__(self, x, y, packman_pos):

        super(Ghost, self).__init__(x, y, GHOST_FILE)	

        self.packman_pos = packman_pos
        self.blocks = None

        # Set speed vector
        self.change_x          = ZERO
        self.change_y          = ZERO

    def update(self):
    	self.move()

    def move(self):
    	pass