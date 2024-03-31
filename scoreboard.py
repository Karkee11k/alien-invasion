import pygame.font

from ship import Ship


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, screen, settings, stats):
        """Initializes the scoreboard's attributes."""
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.textColor = (60, 60, 60)
        self.font = pygame.font.SysFont(None, 48)

        self.prepHighScore()
        self.prepScore()
        self.prepLevel()
        self.prepShips()

    
    def __getScoreImage(self, score):
        """Turns and returns the score as an image."""
        formattedScore = '{:,}'.format(round(score, -1))
        return self.font.render(formattedScore, True, self.textColor,
                                self.settings.backgroundColor)
        

    def prepScore(self):
        """Turns the score into a rendered image and sets its position."""
        self.scoreImage = self.__getScoreImage(self.stats.score)
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20


    def prepHighScore(self):
        """Turns the high score into a rendered image and sets its position."""
        self.highScoreImage = self.__getScoreImage(self.stats.highScore)
        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = 20


    def prepLevel(self):
        """Turns the level into a rendered image."""
        level = str(self.stats.level)
        self.levelImage = self.font.render(level, True, self.textColor,
                                           self.settings.backgroundColor)
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.scoreRect.right
        self.levelRect.top = self.scoreRect.bottom + 10


    def prepShips(self):
        """Shows how may ships left."""
        self.ships = [] 
        for i in range(self.stats.shipsLeft):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 10 + i * ship.rect.width 
            ship.rect.y = 10
            self.ships.append(ship)


    def decreaseShips(self):
        """Decreases the ships."""
        self.ships.pop()


    def showScore(self):
        """Draws the score to the screen."""
        self.screen.blit(self.scoreImage, self.scoreRect)


    def showHighScore(self):
        """Draws the high score to the screen."""
        self.screen.blit(self.highScoreImage, self.highScoreRect)

    
    def showLevel(self):
        """Draws the level to the screen."""
        self.screen.blit(self.levelImage, self.levelRect)


    def showShips(self):
        """Draws the ships to the screen."""
        for ship in self.ships:
            ship.blitme()