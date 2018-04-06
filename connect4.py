import numpy as np
import pygame
import sys
import math

ROW = 6
COLUMN = 7
BLUE = (0, 0, 255)			#RGB 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GOLD = (255,215,0)

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
			

board = create_board()                 		#Initialise the board(First time)
print_board(board)							

game_over = False 							#Game_Flag 
turn = 0									#Player_Flag 
draw_game = int(0)							#DRAW GAME CHECK

pygame.init()

SQUARESIZE = 100
width = COLUMN * SQUARESIZE
height = (ROW+1) * SQUARESIZE				#+1 FOr DISPLAY SCREEN which shows where the chip is to be dropped

size = (width, height)
RADIUS = int(SQUARESIZE/2 -5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("Monospace",75)
draw = pygame.font.SysFont("Monospace",75)

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
				label = draw.render("GAME DRAW!!!!",1,GOLD)
				screen.blit(label, (40,10))
				game_over = True

			print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2

			if game_over:
				pygame.time.wait(3000)

			



	