import pygame

from pygame.locals import *


BLUE = (50, 50, 255)

class Block(pygame.sprite.Sprite):

	def __init__(self, x, y, width, height):
		""" Constructor for the wall that the player can run into. """
		# Call the parent's constructor
		super().__init__()
 
		# Make a blue wall, of the size specified in the parameters
		self.image = pygame.Surface([width, height])
		self.image.fill(BLUE)
 
		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x