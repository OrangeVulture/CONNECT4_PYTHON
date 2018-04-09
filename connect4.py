import numpy as np 			#Using flip funtion, to flip the board
import pygame				#Main game runs with this library
import sys 					#sys.exit()
import math 				#For floor function
import os 					#For environ function, to position window at center
import time

#COLOR CONSTANTS
BLUE = (0, 0, 255)			#RGB 
BLACK = (0, 0, 0)
red = (200,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GOLD = (255,215,0)
green = (0, 200, 0)
GREEN = (0, 255, 0)
B_RED = (255, 0, 0)
GREY = (211,211,211)

#PROGRAM CONSTANTS
ROW = 6
COLUMN = 7
FPS = 30			#FOR clock - FOR INSTRUCTIONS

#PROGRAM INITIALIZATIONS
os.environ['SDL_VIDEO_CENTERED'] = '1'					#To position the pygame window at the center
SQUARESIZE = 100
width = COLUMN * SQUARESIZE
height = (ROW+1) * SQUARESIZE				#+1 FOr DISPLAY SCREEN which shows where the chip is to be dropped
RADIUS = int(SQUARESIZE/2 -5)
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

display_width = 800
display_height = 600
# gameDisplay = pygame.display.set_mode((width,height))



#GAME FUNCTIONS

def create_board():
	board = np.zeros((ROW,COLUMN))       	#Putting zero in all the rows and columns
	return board 

def drop_piece(board, row, col, piece):		#Drops the chip
	board[row][col] = piece
def is_valid_location(board, col): 			#Returns True if chip can be placed in any row for a particular column
	return board[ROW-1][col] == 0
def get_next_open_row(board, col):  		#Seeing which row is empty in a particular column
	for r in range(ROW) :
		if board[r][col] == 0 :
			return r
def print_board(board):						#For flipping board, as chips start from the bottom of the board and array starts from top of board
	print(np.flip(board,0))             	#1 - Horizontal  0- Vertical FLIP (numpy)

def chicken_dinner(board,piece):
	#HORIZONTAL WIN
	for c in range(COLUMN-3):
		for r in range(ROW):
			if(board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece):
				return True
	#VERTICAL WIN
	for c in range(COLUMN):
		for r in range(ROW-3):
			if(board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece):
				return True

	#FORWARD SLASH WIN
	for c in range(COLUMN-3):
		for r in range(ROW-3):
			if(board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece):
				return True
	#BACKWARD SLASH WIN
	for c in range(COLUMN-3):
		for r in range(3,ROW):											#Starts from 3 as win can't occur before 3rd row
			if(board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece):		#r gets decremented because we go down the row in this win
				return True

def draw_board(board):
	for c in range(COLUMN):
		for r in range(ROW):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))   #DRAWING RECTANGLE
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2) , int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), RADIUS)    #DRAWING CIRCLES
			

	for c in range(COLUMN):
		for r in range(ROW):
			if(board[r][c]==1):
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2) , height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS)
			elif(board[r][c]==2):
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2) , height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS)
	
	pygame.display.update()



#GUI FUNCTIONS


def button(msg, x, y, w, h, ic, ac, act="NONE"):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()	

	mybut = pygame.font.SysFont("Monospace",20)

	if((x+w > mouse[0] > x) & (y+h > mouse[1] > y)):
		pygame.draw.rect(screen, ac, (x,y,w,h))      #gameDisplay
		if(click[0] == 1 and act != "NONE"):
			if(act == "PLAY"):
				pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))				#Small_bug, To HIde Connect-4 TEXT in the Black rect area until mouse is not updated
				game_loop()
			elif(act == "INST"):
				text="             INSTRUCTIONS\nSummary:\nIf your looking for a simple strategy game that can be played with just " \
					"about anyone, including young children, Connect Four is for you. \nConnect Four is a " \
				    "simple game similar to Tic-Tac-Toe. \nOnly instead of three in a row, the winner must " \
				    "connect four in a row. \nDue to the nature of the game setup, Connect Four is a little more "\
				    "hands on and fun for younger kids to drop their checkers down the slots. \nConnect Four is a simple "\
				    "and fun two player game that only takes minutes to finish. "\
				    "\nObject:\nTo win Connect Four you must be the first player to get four of your colored checkers in a "\
				    "row either horizontally, vertically or diagonally."
				instructions(clock, screen, text)
			elif(act == "CRED"):
				credits()
			elif(act == "BACK"):
				game_intro()
			elif(act == "EXIT"):
				pygame.quit()
				quit()
	else:
		pygame.draw.rect(screen, ic, (x,y,w,h))		#gameDisplay
		
	textSurface, textRect = text_objects(msg,mybut)
	textRect.center = (x+(w/2),y+(h/2))
	screen.blit(textSurface, textRect) 				#gameDisplay


def blit_text(surface, text, pos, font, color=pygame.Color('black')):						#FOR INSTRUCTIONS
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def instructions(clock, screen, text ):
    font = pygame.font.SysFont('Monospace', 25)
    while True:

        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(GREY)
        blit_text(screen, text, (20, 20), font)
        button("BACK",300,600,100,50,red, RED, "BACK")
        pygame.display.update()




def credits():
	screen.fill(GREY)
	message_display("CREDITS",100)
	message_display("AHAN",300)
	message_display("FREDDY",375)
	message_display("JITHIN",450)
	message_display("JOSEPH",525)
	message_display("VAIBHAV",600)



def message_display(text, y):
    myfont = pygame.font.SysFont("Monospace",75)
    TextSurf, TextRect = text_objects(text, myfont)
    TextRect.center = ((width/2),y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)





def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def game_intro():

	pygame.init()

	intro = True
	
	myfont = pygame.font.SysFont("Monospace",75)

	
	
	while intro :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		screen.fill(GREY)											#gameDisplay
		
		TextSurf, TextRect = text_objects("CONNECT-4", myfont)
		TextRect.center = ((width/2),(height/8))
		screen.blit(TextSurf, TextRect)								#gameDisplay

		button("PLAY",280,200,140,70, green, GREEN,"PLAY")

		button("INSTRUCTIONS",280,300,140,70, green, GREEN,"INST")

		button("CREDITS",280,400,140,70, green, GREEN,"CRED")

		button("EXIT",280,500,140,70, red, RED,"EXIT")

		pygame.display.update()
		# clock.tick(5)



			
			
def game_loop():						#Function in loop to run the game
	
	# os.environ['SDL_VIDEO_CENTERED'] = '1'				#To position the pygame window at the center

	board = create_board()                 		#Initialise the board(First time)
	print_board(board)				
	draw_board(board)
	pygame.display.update()

	myfont = pygame.font.SysFont("Monospace",75)
	# draw = pygame.font.SysFont("Monospace",75)

	game_over = False 							#Game_Flag 
	turn = 0									#Player_Flag 
	draw_game = int(0)							#DRAW GAME CHECK

	while not game_over:
		for event in pygame.event.get(): 			#detects any movement from mouse
			if(event.type == pygame.QUIT):
				sys.exit()

			if(event.type == pygame.MOUSEMOTION):
				pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
				posx = event.pos[0]
				if turn == 0 :
					pygame.draw.circle(screen,RED,(posx, int (SQUARESIZE/2)),RADIUS)
				else :
					pygame.draw.circle(screen,YELLOW,(posx, int(SQUARESIZE/2)),RADIUS)
				pygame.display.update()

			if(event.type == pygame.MOUSEBUTTONDOWN):
				pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
				if turn == 0:                    		#Player 1(turn = even or 0)
					posx = event.pos[0]					
					col = int(math.floor(posx/SQUARESIZE)) 		#Detects column to be put in

					if is_valid_location(board,col):
					 	row = get_next_open_row(board,col)
					 	drop_piece(board,row,col,1)

					 	if(chicken_dinner(board,1)):
					 		label = myfont.render("Player 1 wins!!",1,RED)
					 		screen.blit(label, (40,10))
					 		game_over = True

				else:                                 #Player 2(turn = odd or 1)
					posx = event.pos[0]					
					col = int(math.floor(posx/SQUARESIZE))    #Detects column to be put in

					if is_valid_location(board,col):
					 	row = get_next_open_row(board,col)
					 	drop_piece(board,row,col,2)

					 	if(chicken_dinner(board,2)):
					 		label = myfont.render("Player 2 wins!!",1,YELLOW)
					 		screen.blit(label, (40,10))
					 		game_over = True 

				#For checking draw game condition
				draw_game = int(draw_game + 1)
				if(draw_game == ROW*COLUMN):
					#pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
					label = myfont.render("GAME DRAW!!!!",1,GOLD)
					screen.blit(label, (40,10))
					game_over = True

				print_board(board)
				draw_board(board)

				turn += 1
				turn = turn % 2

				if game_over:
					pygame.time.wait(3000)


				


game_intro()
		
