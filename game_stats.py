class GameStats:
    """ A class to track statistics for Alien Invasion."""

    def __init__(self, settings):
        """Initializes the statistics."""
        self.settings = settings 
        self.gameActive = False
        self.highScore = 0
        self.resetStats()

    
    def resetStats(self):
        """Initializes the stats that can change during the game."""
        self.shipsLeft = self.settings.shipsLimit
        self.score = 0
        self.level = 0