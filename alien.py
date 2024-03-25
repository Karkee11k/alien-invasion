import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent an alien in the fleet."""

    def __init__(self, screen, settings):
        """Initializes the alien and set its position."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        """Updates the ship's position."""
        self.x += self.settings.alienSpeed * self.settings.fleetDirection
        self.rect.x = self.x
         
    def hitEdges(self):
        """Returns true if the alien is at the edge of screen."""
        screenRight = self.screen.get_rect().right
        return self.rect.right >= screenRight or self.rect.left <= 0

    
    def blitme(self):
        """Draws the alien on the screen at its current position."""
        self.screen.blit(self.image, self.rect)