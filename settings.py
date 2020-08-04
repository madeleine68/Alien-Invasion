class Settings:
	"""A class to store all settings for Alien Invasion """
	def __init__(self):
		"""Initialized the gams's setting"""
		# Screen setting
		self.screen_width = 800
		self.screen_height = 500
		self.bg_color = (255,255,250)

		# Ship setting
		self.ship_speed = 1.5

		# Bullet setting
		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (250,189,46)
		self.bullet_allowed = 3


		
		