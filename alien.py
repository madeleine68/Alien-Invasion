import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	""" A class to represent a single alien in the fleet"""

	def ___init__(self, ai_game):
		"""Intialized the alien and set its rect attribute"""
		super().__init__()
		self.screen = ai_game.screen

		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load ('/Users/mahdieh/Desktop/Alien_game/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal pposition.
		self.x= float(self.rect.x)


