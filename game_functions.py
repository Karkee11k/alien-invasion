from time import sleep
import pygame 
import sys 

from alien import Alien
from bullet import Bullet


def checkEvents(screen, settings, stats, playButton, ship, aliens, bullets):
	"""Responds to events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			checkKeydown(event, screen, settings, stats, ship, aliens, playButton, 
				bullets)
		elif event.type == pygame.KEYUP:
			checkKeyup(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			checkPlayButton(screen, settings, stats, ship, aliens, bullets,
				   playButton, x, y)


def checkPlayButton(screen, settings, stats, ship, aliens, bullets, 
					playButton, x, y):
	"""Responds to the 'PLAY' button."""
	clicked = playButton.rect.collidepoint(x, y)
	if clicked and not stats.gameActive:
		stats.gameActive = True
		stats.resetStats()
		aliens.empty()
		bullets.empty()
		createFleet(screen, settings, ship, aliens)


def checkKeydown(event, screen, settings, stats, ship, aliens, playButton, 
				 bullets):
	"""Respond to key presses."""
	if event.key == pygame.K_q:
		sys.exit()
	if event.key == pygame.K_RIGHT:
		ship.movingRight = True 
	elif event.key == pygame.K_LEFT:
		ship.movingLeft = True
	elif event.key == pygame.K_SPACE:
		fireBullets(screen, settings, ship, bullets)
	elif event.key == pygame.K_p:
		x, y = playButton.rect.x, playButton.rect.y
		checkPlayButton(screen, settings, stats, ship, aliens, bullets, 
				  playButton, x, y)


def checkKeyup(event, ship):
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		ship.movingRight = False 
	elif event.key == pygame.K_LEFT:
		ship.movingLeft = False


def updateScreen(screen, settings, stats, playButton, ship, aliens, bullets):
	"""Updates the screen."""
	screen.fill(settings.backgroundColor)
	for bullet in bullets.sprites():
		bullet.drawBullet()
	ship.blitme()
	aliens.draw(screen)
	if not stats.gameActive:
		playButton.drawButton()
	pygame.display.flip() 
	
	
def updateBullets(screen, settings, ship, aliens, bullets):
	"""Updates position of bullets and gets rid of old bullets."""
	bullets.update()

	# Get rid of disappeared bullets
	disappearedBullets = [bullet for bullet in bullets if bullet.isDisappeared()]
	for disappearedBullet in disappearedBullets:
		bullets.remove(disappearedBullet)

	# Check for bullets that have hit an alien
	checkAlienBulletCollisions(screen, settings, ship, aliens, bullets)
		

def checkAlienBulletCollisions(screen, settings, ship, aliens, bullets):
	"""Respond to bullet alien collision."""
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	# If all the aliens shot, repopulating the fleet
	if len(aliens) == 0:
		bullets.empty()
		createFleet(screen, settings, ship, aliens)


def fireBullets(screen, settings, ship, bullets):
	"""Fires a bullet if the limit is not reached."""
	if len(bullets) < settings.bulletsAllowed:
		bullets.add(Bullet(screen, settings, ship))


def createFleet(screen, settings, ship, aliens):
	"""Creates a fleet of aliens."""
	alien = Alien(screen, settings)
	aliensPlacedY = numberOfAliensY(settings, ship.rect.height, 
								 alien.rect.height) 
	aliensPlacedX = numberOfAliensX(settings, alien.rect.width)

	# Create the first row of the fleet
	for rowNumber in range(aliensPlacedY):
		for alienNumber in range(aliensPlacedX):
			createAlien(screen, settings, aliens, alienNumber, rowNumber)
		

def numberOfAliensX(settings, alienWidth):
	"""Returns number of aliens that fits in a row."""
	availabeSpaceX = settings.screenSize[0] - 2 * alienWidth
	return availabeSpaceX // (2 * alienWidth)


def numberOfAliensY(settings, shipHeight, alienHeight):
	"""Returns the number of rows of aliens that fits on the screen."""
	availableSpaceY = settings.screenSize[1] - 3 * alienHeight - shipHeight
	return availableSpaceY // (2 * alienHeight)


def createAlien(screen, settings, aliens, alienNumber, rowNumber):
	"""Creates an alien and places it in the row."""
	alien = Alien(screen, settings)
	alienWidth, alienHeight = alien.rect.width, alien.rect.height
	alien.x = alienWidth + 2 * alienWidth * alienNumber
	alien.rect.x = alien.x
	alien.y = alienHeight + 2 * alienHeight * rowNumber
	alien.rect.y = alien.y
	aliens.add(alien)


def checkFleetEdges(settings, aliens):
	"""Responds appropriately if any aliens hit edges."""
	for alien in aliens.sprites():
		if alien.hitEdges():
			changeFleetDirection(settings, aliens)
			break


def changeFleetDirection(settings, aliens):
	"""Drops the entire fleet and changes the fleet's direction."""
	for alien in aliens.sprites():
		alien.rect.y += settings.alienDropSpeed
	settings.fleetDirection *= -1


def updateAliens(screen, settings, stats, ship, aliens, bullets):
	"""Updates the movement of the alien fleet."""
	checkFleetEdges(settings, aliens)
	aliens.update()

	# Respond to alien ship collision
	if pygame.sprite.spritecollideany(ship, aliens):
		shipHit(screen, settings, stats, ship, aliens, bullets)
	checkAliensBottom(screen, settings, stats, ship, aliens, bullets)


def shipHit(screen, settings, stats, ship, aliens, bullets):
	"""Responds to ship being hit by alien."""
	bullets.empty()
	aliens.empty()

    # New Fleet of aliens and center the ship
	createFleet(screen, settings, ship, aliens)
	ship.centerShip()

	if stats.shipsLeft > 1:
		stats.shipsLeft -= 1
		sleep(.5)
	else:
		stats.gameActive = False


def checkAliensBottom(screen, settings, stats, ship, aliens, bullets):
	"""Responds to aliens reached the bottom of the screen."""
	screenRect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screenRect.bottom:
			shipHit(screen, settings, stats, ship, aliens, bullets)
			break