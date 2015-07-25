import gameobj

from colors import BLUE

class Block(gameobj.GameObj):

	def __init__(self, x, y, width, height):
		""" Constructor for the wall that the player can run into. """
		# Call the parent's constructor
		super(Block, self).__init__(x, y)
 
		# Make a blue wall, of the size specified in the parameters
		self.image = gameobj.pygame.Surface([width, height])
		self.image.fill(BLUE)
 
		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y