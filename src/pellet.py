#from block import *
import pygame
from pygame import gfxdraw

GOLD       = (255,215,0)
GOLDEN_ROD = (218,165,32)
RADIUS     = 8


PELLET_IMAGE_FILE        = "../resources/sprites/pellet.png"


class Pellet(pygame.sprite.Sprite):

	def __init__(self, x, y, energized, surface):
		#super(Pellet, self).__init__(x, y, width, height)
		# Call the parent's constructor
		super().__init__()
		if energized:
			color = GOLD
		else:
			color = GOLDEN_ROD

		self.image             = pygame.image.load(PELLET_IMAGE_FILE)
		self.rect              = self.image.get_rect()
		self.rect.x            = x
		self.rect.y            = y

		"""
		pygame.gfxdraw.aacircle(surface, x, y, 3, color)
		pygame.gfxdraw.filled_circle(surface, x, y, 3, color)
		self.rect.x = x
		self.rect.y = y
		"""

		#self.image.fill(color)
		#self.rect = pygame.draw.circle(self.image, color, (x, y), RADIUS, 8)
		self.energized = energized

