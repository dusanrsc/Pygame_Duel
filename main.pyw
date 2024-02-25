# importing sub-modules
from classes import *
from functions import *

def main():
	# importing variables from settings.pyw
	# because main is reading as python module in this case
	from settings import p1_health, p2_health, image_show, p1_bullet_active, p2_bullet_active

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

	# creating instances of the bullet classes
	p1b = P1B(pos_x=player1.rect.x + 40, pos_y=player1.rect.y + 25)
	p2b = P2B(pos_x=player2.rect.x + 10, pos_y=player2.rect.y + 25)

	# create buttons instances
	play_button = Button(x=300, y=120, width=100, height=30, bg_color=BLUE, text="Play", text_color=BLACK)
	quit_button = Button(x=400 + LINE_TICKNESS, y=120, width=100, height=30, bg_color=RED, text="Quit", text_color=BLACK)

	# start screen control display
	# loading images
	player1_controles = pygame.image.load("sprites/controles1.png").convert()
	player2_controles = pygame.image.load("sprites/controles2.png").convert()

	# converting alpha (setting up image transparency)
	player1_controles.set_colorkey(ALPHA)
	player2_controles.set_colorkey(ALPHA)

	# defining a font
	my_font = pygame.font.SysFont("Comic Sans MS", 100)

	# main game loop
	while running:
		# defining a text
		# have to be inside the while loop for constant color changing
		blue_win = my_font.render("BLUE WIN", False, ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))))
		red_win = my_font.render("RED WIN", False, ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))))

		# if key pressed statements
		# if exit button is clicked
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# triggering exit game function
				exit()

			# if any key pressed 
			if event.type == pygame.KEYDOWN:
				# displaying start game image off
				image_show = False

			# check for button click
			if event.type == pygame.MOUSEBUTTONDOWN:
				if play_button.rect.collidepoint(event.pos):
					# on left mouse click button function
					# play again function
					# activating main function
					main()

				if quit_button.rect.collidepoint(event.pos):
					# on left mouse click button function
					# triggering exit game function
					exit()

		# pressed keys
		keys = pygame.key.get_pressed()

		# pressed keys for player 1
		if keys[pygame.K_SPACE] and p1_bullet_active == True:
			p1b = P1B(pos_x=player1.rect.x + 30, pos_y=player1.rect.y + 25)
			p1b_group.add(p1b)

		# player 1 movement on key press
		if keys[pygame.K_w]:
			player1.rect.y -= PLAYER_SPEER
		if keys[pygame.K_s]:
			player1.rect.y += PLAYER_SPEER
		if keys[pygame.K_a]:
			player1.rect.x -= PLAYER_SPEER
		if keys[pygame.K_d]:
			player1.rect.x += PLAYER_SPEER

		# pressed keys for player 2
		if keys[pygame.K_RSHIFT] and p2_bullet_active == True:
			p2b = P2B(pos_x=player2.rect.x + 10, pos_y=player2.rect.y + 25)
			p2b_group.add(p2b)

		# player 1 movement on key press
		if keys[pygame.K_UP]:
			player2.rect.y -= PLAYER_SPEER
		if keys[pygame.K_DOWN]:
			player2.rect.y += PLAYER_SPEER
		if keys[pygame.K_LEFT]:
			player2.rect.x -= PLAYER_SPEER
		if keys[pygame.K_RIGHT]:
			player2.rect.x += PLAYER_SPEER

		# collision section
		# if player 1 bullet hit player 2
		if pygame.sprite.groupcollide(p2b_group, player1_group, True, False, pygame.sprite.collide_rect_ratio(.9)):
			p1_health -= 1

		# if player 2 bullet hit player 1
		if pygame.sprite.groupcollide(p1b_group, player2_group, True, False, pygame.sprite.collide_rect_ratio(.9)):
			p2_health -= 1

		# bullet collision
		if pygame.sprite.groupcollide(p1b_group, p2b_group, True, True, pygame.sprite.collide_rect_ratio(.9)):
			pass

		# drawing sprites on the screen
		SCREEN.fill(BLACK)

		# drawing and updating for player 1 bullet
		p1b_group.update()
		p1b_group.draw(SCREEN)

		# drawing and updating for player 2 bullet
		p2b_group.update()
		p2b_group.draw(SCREEN)

		# drawing and updating for player 1
		player1_group.update()
		player1_group.draw(SCREEN)

		# drawing and updating for player 2
		player2_group.update()
		player2_group.draw(SCREEN)

		# drawing green marker on the screen
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

		# drawing buttons logic
		# if player 1 or player 2 have 0 healths (lose game)
		if p1_health <= 0 or p2_health <= 0:
			play_button.draw()
			quit_button.draw()

		# logic for showing start screen image
		if image_show == True:
			# drawing start screen control display
			SCREEN.blit(player1_controles, (120, 200))
			SCREEN.blit(player2_controles, (480, 200))
		else:
			# logic for restricting start screen control display drawing on the screen 
			pass

		# game over
		# player 1 lose
		if p1_health <= 0:
			# opponent player health is maximum
			p2_health = 50
			# player 1 not able to fireing bullets
			p1_bullet_active = False
			# destroying opponent player
			player1.kill()
			# destroying opponent bullets
			p1b.kill()
			# marker changing collor to winner collor
			marker(RED)
			# displaying red player win message
			SCREEN.blit(red_win, (175, 200))

		# player 2 lose
		if p2_health <= 0:
			# opponent player health is maximum
			p1_health = 50
			# player 2 not able to fireing bullets
			p2_bullet_active = False
			# destroying opponent player
			player2.kill()
			# destroying opponent bullets
			p2b.kill()
			# marker changing collor to winner collor
			marker(BLUE)
			# displaying blue player win message
			SCREEN.blit(blue_win, (140, 200))

		# updating the screen and fps counter
		pygame.display.flip()
		pygame.time.Clock().tick(FPS)

# starting the game
# this condition reading current file as python module
if __name__ == "__main__":
	main()