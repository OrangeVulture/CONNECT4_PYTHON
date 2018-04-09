import pygame
import time
import os

grey = (211,211,211)
red = (200,0,0)
b_red = (255, 0, 0)
green = (0,200,0)
b_green = (0, 255, 0)
black = (0,0,0)
blue = (0, 0, 255)

def button(msg, x, y, w, h, ic, ac):

	mouse = pygame.mouse.get_pos()

	mybut = pygame.font.SysFont("Monospace",20)

	if((x+w > mouse[0] > x) & (y+h > mouse[1] > y)):
		pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
	else:
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
		
	textSurface, textRect = text_objects(msg,mybut)
	textRect.center = (x+(w/2),y+(h/2))
	gameDisplay.blit(textSurface, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
	intro = True
	clock = pygame.time.Clock()
	myfont = pygame.font.SysFont("Monospace",75)
	
	
	while intro :
		for event in pygame.event.get():
			# print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		gameDisplay.fill(grey)
		
		TextSurf, TextRect = text_objects("CONNECT-4", myfont)
		TextRect.center = ((display_width/2),(display_height/8))
		gameDisplay.blit(TextSurf, TextRect)

		button("PLAY",325,200,140,70,green,b_green)

		button("INSTRUCTIONS",325,300,140,70,green,b_green)

		button("CREDITS",325,400,140,70,green,b_green)

		button("EXIT",325,500,140,70,red,b_red)

		pygame.display.update()
		clock.tick(15)

os.environ['SDL_VIDEO_CENTERED'] = '1'					#To position the pygame window at the center
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.init()

game_intro()



pygame.exit()
