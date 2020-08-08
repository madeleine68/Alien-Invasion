class Settings:
	"""A class to store all settings for Alien Invasion """
	def __init__(self):
		"""Initialized the gams's setting"""
		# Screen setting
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255,255,250)

		# Ship setting
		self.ship_speed = 1.5

		# Bullet setting
		self.bullet_speed = 2
		self.bullet_width = 5
		self.bullet_height = 10
		self.bullet_color = (250,189,46)
		self.bullet_allowed = 3
		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1


		
		