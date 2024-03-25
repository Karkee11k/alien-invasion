import pygame.font


class Button:
    """A class to represent buttons."""

    def __init__(self, screen, msg):
        """Initializes the button attributes."""
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.width, self.height = 200, 50
        self.buttonColor = (0, 255, 0)
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center
        self.prepMsg(msg)


    def prepMsg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.image = self.font.render(msg, True, self.textColor)
        self.imageRect = self.image.get_rect()
        self.imageRect.center = self.rect.center

  
    def drawButton(self):
        """Draws the button on the screen."""
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.image, self.imageRect)