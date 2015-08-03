import gameobj
import math

from colors import BLACK, GOLDEN_ROD, GREEN

ZERO = 0

class Ghost(gameobj.GameObj):

    def __init__(self, x, y, image, packman_pos):

        super(Ghost, self).__init__(x, y, image)	

        self.packman_pos = packman_pos
        self.blocks = None

        # Set speed vector
        self.velX          = ZERO
        self.velY          = ZERO

    def getAngle(self):
        # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
        angle = math.atan2(self.rect.x - self.packman_pos[0], self.rect.y - self.packman_pos[1]) # get the angle in radians
        angle = angle * (180 / math.pi) # convert to degrees
        angle = (angle + 90) % 360 # adjust for a right-facing sprite
        return angle

    def draw(self, screen):
        degrees = self.getAngle()
        #print(degrees)
        # draw the outline of the eye
        gameobj.pygame.draw.circle(self.image, GREEN, (self.rect.x, self.rect.y), 20, 3)

        # draw the black part of the eye
        xPos = math.cos(degrees * (math.pi / 180)) * 5
        yPos = math.sin(degrees * (math.pi / 180)) * 5
        gameobj.pygame.draw.circle(self.image, GREEN, (int(xPos) + self.rect.x, -1 * int(yPos) + self.rect.y), 15)


    def update(self):
    	self.move()

    def move(self):
    	pass