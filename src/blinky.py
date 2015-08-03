import ghost

BLINKY_FILE = "../resources/sprites/blinky.png"
BLINKY_STEP = 2

class Blinky(ghost.Ghost):

	def __init__(self, x, y, packman_pos):
		super(Blinky, self).__init__(x, y, BLINKY_FILE, packman_pos)

		self.velX = BLINKY_STEP
		self.velY = BLINKY_STEP

	def move(self):
		if self.rect.x < self.packman_pos[0]:
			self.rect.x += BLINKY_STEP
		elif self.rect.x > self.packman_pos[0]:
			self.rect.x -= BLINKY_STEP
		self._collide_with_blocks_x()

		if self.rect.y < self.packman_pos[1]:
			self.rect.y += BLINKY_STEP
		elif self.rect.y > self.packman_pos[1]:
			self.rect.y -= BLINKY_STEP
		self._collide_with_blocks_y()
	