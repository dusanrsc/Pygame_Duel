# importing sub-modules
from settings import *

# game classes
# class player
class Player1(pygame.sprite.Sprite):
	def __init__(self, pos_x=50, pos_y=300):
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
	def __init__(self, pos_x=750, pos_y=300):
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
# class bullet for player 1
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

# class bullet for player 2
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

# button class
class Button(object):
	def __init__(self, x=0, y=0, width=100, height=30, bg_color=YELLOW, text="Click", text_color=BLACK):
		self.rect = pygame.Rect(x, y, width, height)
		self.bg_color = bg_color
		self.text = text
		self.text_color = text_color

	# drawing method of the button class
	def draw(self):
		pygame.draw.rect(SCREEN, self.bg_color, self.rect)
		font = pygame.font.Font(None, 36)
		text = font.render(self.text, True, self.text_color)
		text_rect = text.get_rect(center=self.rect.center)
		SCREEN.blit(text, text_rect)