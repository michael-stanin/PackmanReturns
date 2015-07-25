import gameobj


RADIUS     = 8


PELLET_IMAGE_FILE        = "../resources/sprites/pellet.png"


class Pellet(gameobj.GameObj):

	def __init__(self, x, y, energized):
		#super(Pellet, self).__init__(x, y, width, height)
		# Call the parent's constructor
		super().__init__(x, y, PELLET_IMAGE_FILE)
		self.energized = energized

