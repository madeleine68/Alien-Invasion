import sys 
import pygame
from settings import Settings
from ship import Ship

class AlienInvension:
	"""Overaal class to manage game assets and behavoir"""
	def __init__ (self):
		"""Initialized the game, and create game resourses"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invension") 

		self.ship = Ship(self)

	def run_game (self):
	   """Start the main loop for the game"""
	   while True:
	   	# watch for keyboard and mouse events.
	   	self._check_events()
	   	self._update_screen()

	def _check_events (self):
	   """respond to keypresses and mouse events"""
	   for event in pygame.event.get():
	   	   if event.type == pygame.QUIT:
	   	      sys.exit()
	   	      
	def _update_screen (self):
	   #update images on screen and flip to the new screen
	   self.screen.fill(self.settings.bg_color)
	   self.ship.blitme()      

	   #make the most recently drwan screen visible.
	   pygame.display.flip()


if __name__ == '__main__':
	#make a game instance and run the game
	ai = AlienInvension()
	ai.run_game()


	







