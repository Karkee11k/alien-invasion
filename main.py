import pygame 
from pygame.sprite import Group

from game_stats import GameStats
from settings import Settings
from ship import Ship
import game_functions as gf
from button import Button


def run():
	"""Initializes the game and creates a screen object.""" 
	pygame.init() 
	settings = Settings()
	screen = pygame.display.set_mode(settings.screenSize) 
	pygame.display.set_caption('Alien Invasion') 
	ship = Ship(screen, settings)
	aliens = Group()
	bullets = Group()
	stats = GameStats(settings)
	playButton = Button(screen, 'PLAY')
	gf.createFleet(screen, settings, ship, aliens)

	while True: 
		gf.checkEvents(screen, settings, stats, playButton, ship, aliens, 
				 bullets)
		if stats.gameActive:
			ship.update()
			gf.updateBullets(screen, settings, ship, aliens, bullets)
			gf.updateAliens(screen, settings, stats, ship, aliens, bullets)
		gf.updateScreen(screen, settings, stats, playButton, ship, aliens, bullets)
		
	
run()