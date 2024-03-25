class Settings: 
	"""A class to store all the settings for Alien Invasion.""" 
	
	def __init__(self): 
		"""Initialize the game's settings.""" 
		self.screenSize = (1200, 700)
		self.backgroundColor = (230, 230, 230)

		# Ship settings
		self.shipSpeed = 1.5
		self.shipsLimit = 3

		# Bullet settings
		self.bulletSpeed = 3
		self.bulletColor = (60, 60, 60)
		self.bulletWidth = 3
		self.bulletHeight = 15
		self.bulletsAllowed = 3

		# Alien settings
		self.alienSpeed = 1
		self.fleetDirection = 1 # 1 to right, -1 to left
		self.alienDropSpeed = 10