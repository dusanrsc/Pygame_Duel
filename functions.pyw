# importing sub-modules
from settings import *

# game functions
# exit game function
def exit():
	pygame.quit()
	sys.exit()
	running = False

# drawing game boundaries function
def marker(color=GREEN):
	pygame.draw.rect(SCREEN, color, (0, 0, 800, 600), LINE_TICKNESS)
	pygame.draw.line(SCREEN, color, (400, 0), (400, 600), LINE_TICKNESS)

# health bar function
def health_bar(pos_x, pos_y, health=50):
	# if health greather than zero draw health bar
	if health > 0:
		bar = pygame.draw.rect(SCREEN, GREEN, (pos_x, pos_y - 15, health, 8))
		frame = pygame.draw.rect(SCREEN, WHITE, (pos_x, pos_y - 15, 50, 8), LINE_TICKNESS)
	# else not draw just pass
	else:
		pass