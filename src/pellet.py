from block import *


class Pellet(Block):

	def __init__(self, x, y, image, energized=False):
		super(Pellet, self).__init__(x, y, image)
		self.energized = energized