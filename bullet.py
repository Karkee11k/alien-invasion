import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, screen, settings, ship):
        """Creates a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.bulletWidth,
                                settings.bulletHeight)      
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = settings.bulletColor
        self.speed = settings.bulletSpeed


    def update(self):
        """Moves the bullet up the screen."""
        self.y -= self.speed
        self.rect.y = self.y


    def drawBullet(self): 
        """Draws the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


    def isDisappeared(self):
        """Returns true if the bullet disappeared from the screen."""
        return self.rect.bottom <= 0