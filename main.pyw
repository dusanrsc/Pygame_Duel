# importing files
from settings import *

# game classes
# class player
class Player1(pygame.sprite.Sprite):
	def __init__(self, pos_x=50, pos_y=275):
		super().__init__()
		self.image = pygame.image.load("sprites/p1.png").convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	# update method
	def update(self):
		# restricting movement
		if self.rect.x >= 350:
			self.rect.x = 350
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.y <= 0:
			self.rect.y = 0
		if self.rect.y >= 550:
			self.rect.y = 550

# class player
class Player2(pygame.sprite.Sprite):
	def __init__(self, pos_x=750, pos_y=275):
		super().__init__()
		self.image = pygame.image.load("sprites/p2.png").convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	# update method
	def update(self):
		# restricting movement
		if self.rect.x <= 400:
			self.rect.x = 400
		if self.rect.x >= 750:
			self.rect.x = 750
		if self.rect.y <= 0:
			self.rect.y = 0
		if self.rect.y >= 550:
			self.rect.y = 550

# class bullet
class P1B(pygame.sprite.Sprite):
	def __init__(self, pos_x=0, pos_y=0):
		super().__init__()
		self.image = pygame.image.load("sprites/p1b.png").convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	# update method
	def update(self):
		self.rect.x += BULLET_SPEED

		# destroying bullets
		if self.rect.x >= SCREEN_WIDTH:
			self.kill()

class P2B(pygame.sprite.Sprite):
	def __init__(self, pos_x=0, pos_y=0):
		super().__init__()
		self.image = pygame.image.load("sprites/p2b.png").convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	# update method
	def update(self):
		self.rect.x -= BULLET_SPEED

		# destroying bullets
		if self.rect.x <= 0:
			self.kill()

# game functions
# exit game function
def exit():
	pygame.quit()
	sys.exit()
	running = False

def marker(color):
	pygame.draw.rect(SCREEN, color, (0, 0, 800, 600), 2)
	pygame.draw.line(SCREEN, color, (400, 0), (400, 600), 2)

def health_bar(pos_x, pos_y, health):
	pygame.draw.rect(SCREEN, GREEN, (pos_x, pos_y - 15, health, 8))
	pygame.draw.rect(SCREEN, WHITE, (pos_x, pos_y - 15, 50, 8), 2)

def start_screen():
	player1_controles = pygame.image.load("sprites/controles1.png").convert()
	player2_controles = pygame.image.load("sprites/controles2.png").convert()

	player1_controles.set_colorkey(ALPHA)
	player2_controles.set_colorkey(ALPHA)

	SCREEN.blit(player1_controles, (100, 200))
	SCREEN.blit(player2_controles, (500, 200))

# creating sprite groups
# player sprite group
player1_group = pygame.sprite.Group()
player1 = Player1()
player1_group.add(player1)

# player sprite group
player2_group = pygame.sprite.Group()
player2 = Player2()
player2_group.add(player2)

# bullet group
p1b_group = pygame.sprite.Group()
p2b_group = pygame.sprite.Group()

# main game loop
while running:
	# if key pressed statements
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	# pressed keys
	keys = pygame.key.get_pressed()

	# player 1
	if keys[pygame.K_SPACE]:
		p1b = P1B(pos_x=player1.rect.x + 40, pos_y=player1.rect.y + 25)
		p1b_group.add(p1b)

	if keys[pygame.K_w]:
		player1.rect.y -= PLAYER_SPEER
	if keys[pygame.K_s]:
		player1.rect.y += PLAYER_SPEER
	if keys[pygame.K_a]:
		player1.rect.x -= PLAYER_SPEER
	if keys[pygame.K_d]:
		player1.rect.x += PLAYER_SPEER

	# player 2
	if keys[pygame.K_RSHIFT]:
		p2b = P2B(pos_x=player2.rect.x + 10, pos_y=player2.rect.y + 25)
		p2b_group.add(p2b)

	if keys[pygame.K_UP]:
		player2.rect.y -= PLAYER_SPEER
	if keys[pygame.K_DOWN]:
		player2.rect.y += PLAYER_SPEER
	if keys[pygame.K_LEFT]:
		player2.rect.x -= PLAYER_SPEER
	if keys[pygame.K_RIGHT]:
		player2.rect.x += PLAYER_SPEER

	# checking for collision
	# if player 1 bullet hit player 2
	if pygame.sprite.groupcollide(p2b_group, player1_group, True, False, pygame.sprite.collide_rect_ratio(.9)):
		p1_health -= 1

	# if player 2 bullet hit player 1
	if pygame.sprite.groupcollide(p1b_group, player2_group, True, False, pygame.sprite.collide_rect_ratio(.9)):
		p2_health -= 1

	# bullet collision
	if pygame.sprite.groupcollide(p1b_group, p2b_group, True, True, pygame.sprite.collide_rect_ratio(.9)):
		pass

	# game over
	# player 1 lose
	if p1_health <= 0:
		p1_health = 0
		player1.kill()

	# player 2 lose
	if p2_health <= 0:
		p2_health = 0
		player2.kill()

	# drawing sprites on the screen
	SCREEN.fill(BLACK)

	# player 1 bullet
	p1b_group.update()
	p1b_group.draw(SCREEN)

	# player 2 bullet
	p2b_group.update()
	p2b_group.draw(SCREEN)

	# player 1
	player1_group.update()
	player1_group.draw(SCREEN)

	# player 2
	player2_group.update()
	player2_group.draw(SCREEN)

	# marking edges with lines
	marker(GREEN)

	# health bars
	# player 1 health bar
	# if player 1 hit top wall health bar is changing position
	if player1.rect.y <= 20:
		player1_health = health_bar(player1.rect.x, player1.rect.y + 72, p1_health)
	else:
		player1_health = health_bar(player1.rect.x, player1.rect.y, p1_health)

	# player 2 health bar
	# if player 2 hit top wall health bar is changing position
	if player2.rect.y <= 20:
		player2_health = health_bar(player2.rect.x, player2.rect.y + 72, p2_health)
	else:
		player2_health = health_bar(player2.rect.x, player2.rect.y, p2_health)

	# displaying start screen controls
	start_screen()

	# updating the screen and fps counter
	pygame.display.flip()
	pygame.time.Clock().tick(FPS)