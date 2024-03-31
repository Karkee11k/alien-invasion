class Settings: 
	"""A class to store all the settings for Alien Invasion.""" 
	
	def __init__(self): 
		"""Initialize the game's settings.""" 
		self.screenSize = (1200, 700)
		self.backgroundColor = (230, 230, 230)
		self.speedUpScale = 1.2
		self.scoreScale = 1.5

		# Ship settings
		self.shipsLimit = 3

		# Bullet settings
		self.bulletColor = (60, 60, 60)
		self.bulletWidth = 3
		self.bulletHeight = 15
		self.bulletsAllowed = 3

		# Alien settings
		self.fleetDirection = 1 # 1 to right, -1 to left
		self.alienDropSpeed = 10

		self.initializeDynamicSettings()


	def initializeDynamicSettings(self):
		"""Initializes the settings that throughout the game."""
		self.shipSpeed = 1.5
		self.bulletSpeed = 3
		self.alienSpeed = 1
		self.points = 50


	def increaseSpeed(self):
		"""Increase the speed of the game."""
		self.shipSpeed *= self.speedUpScale
		self.alienSpeed *= self.speedUpScale
		self.bulletSpeed *= self.speedUpScale
		self.points = int(self.points * self.scoreScale)