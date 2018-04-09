import pygame
import time
import os

GREY = (211,211,211)
RED = (200,0,0)
B_RED = (255, 0, 0)
GREEN = (0,200,0)
B_GREEN = (0, 255, 0)
BLACK = (0,0,0)

def button(msg, x, y, w, h, ic, ac, act="NONE"):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()	

	mybut = pygame.font.SysFont("Monospace",20)

	if((x+w > mouse[0] > x) & (y+h > mouse[1] > y)):
		pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
		if(click[0] == 1 and act != NONE):
			if(act == "PLAY"):
				pass
			elif(act == "INST"):
				pass
			elif(act == "CRED"):
				pass
			elif(act == "EXIT"):
				pygame.quit()
				quit()
	else:
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
		
	textSurface, textRect = text_objects(msg,mybut)
	textRect.center = (x+(w/2),y+(h/2))
	gameDisplay.blit(textSurface, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def game_intro():
	
	
	intro = True
	clock = pygame.time.Clock()
	myfont = pygame.font.SysFont("Monospace",75)
	
	
	while intro :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		gameDisplay.fill(GREY)
		
		TextSurf, TextRect = text_objects("CONNECT-4", myfont)
		TextRect.center = ((display_width/2),(display_height/8))
		gameDisplay.blit(TextSurf, TextRect)

		button("PLAY",325,200,140,70, GREEN, B_GREEN,"PLAY")

		button("INSTRUCTIONS",325,300,140,70, GREEN, B_GREEN,"INST")

		button("CREDITS",325,400,140,70, GREEN, B_GREEN,"CRED")

		button("EXIT",325,500,140,70,RED, B_RED,"EXIT")

		pygame.display.update()
		clock.tick(15)

	


pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'					#To position the pygame window at the center
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

game_intro()

pygame.exit()
