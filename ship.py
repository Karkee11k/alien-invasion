import pygame 

class Ship:
	"""Initialises the ship and sets it starting position."""
	
	def __init__(self, screen, settings):
		"""Includes the image and sets its position."""
		self.screen = screen
		self.settings = settings

		# Load the image and set its rect attribute
		self.image = pygame.image.load('images/ship.bmp')
		self.screenRect = screen.get_rect()
		self.rect = self.image.get_rect()
		self.rect.centerx = self.screenRect.centerx 
		self.center = float(self.rect.centerx)
		self.rect.bottom = self.screenRect.bottom

		# Flags to moving right and left
		self.movingRight = False
		self.movingLeft = False
		

	def update(self):
		"""Updates the ship position."""
		if self.movingRight and self.rect.right < self.screenRect.right:
			self.center += self.settings.shipSpeed
		if self.movingLeft and self.rect.left > 0:
			self.center -= self.settings.shipSpeed
		self.rect.centerx = self.center


	def centerShip(self):
		"""Places the ship at the center of the screen."""
		self.center = self.screenRect.centerx
		self.rect.centerx = self.center


	def blitme(self):
		"""Draws the ship on the screen at its current position."""
		self.screen.blit(self.image, self.rect)	