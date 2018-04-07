import pygame
import time

grey = (211,211,211)
red = (200,0,0)
b_red = (255, 0, 0)
green = (0,200,0)
b_green = (0, 255, 0)
black = (0,0,0)
blue = (0, 0, 255)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
	intro = True
	clock = pygame.time.Clock()
	myfont = pygame.font.SysFont("Monospace",75)
	mybut = pygame.font.SysFont("Monospace",20)
	display_width = 800
	display_height = 600
	
	gameDisplay = pygame.display.set_mode((display_width,display_height))

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

		mouse = pygame.mouse.get_pos()
		# print(mouse)
		if((325+140 > mouse[0] > 325) & (200+70 > mouse[1] > 200)):
			pygame.draw.rect(gameDisplay, b_green, (325,200,140,70))
		else:
			pygame.draw.rect(gameDisplay, green, (325,200,140,70))
		
		textSurface, textRect = text_objects("PLAY",mybut)
		textRect.center = (325+(140/2),200+(70/2))
		gameDisplay.blit(textSurface, textRect)

		if (325+140 > mouse[0] > 325) & (300+70 > mouse[1] > 300) :
			pygame.draw.rect(gameDisplay, b_green, (325,300,140,70))
		else:
			pygame.draw.rect(gameDisplay, green, (325,300,140,70))
		
		textSurface, textRect = text_objects("INSTRUCTIONS",mybut)
		textRect.center = (325+(140/2),300+(70/2))
		gameDisplay.blit(textSurface, textRect)

		if (325+140 > mouse[0] > 325)&(400+70>mouse[1]>400):
			pygame.draw.rect(gameDisplay, b_green, (325,400,140,70))
		else:
			pygame.draw.rect(gameDisplay, green, (325,400,140,70))
		
		textSurface, textRect = text_objects("CREDITS",mybut)
		textRect.center = (325+(140/2),400+(70/2))
		gameDisplay.blit(textSurface, textRect)

		if (325+140 > mouse[0] > 325)&(500+70>mouse[1]>500):
			pygame.draw.rect(gameDisplay, b_red, (325,500,140,70))
		else:
			pygame.draw.rect(gameDisplay, red, (325,500,140,70))

		textSurface, textRect = text_objects("EXIT",mybut)
		textRect.center = (325+(140/2),500+(70/2))
		gameDisplay.blit(textSurface, textRect)

		pygame.display.update()
		clock.tick(15)

pygame.init()

game_intro()

pygame.exit()
