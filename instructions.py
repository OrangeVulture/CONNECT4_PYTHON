import pygame
import time



SIZE = WIDTH, HEIGHT = (1024, 720)
FPS = 30
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()

text="                                                     INSTRUCTIONS\nSummary:\nIf your looking for a simple strategy game that can be played with just " \
    "about anyone, including young children, Connect Four is for you. \nConnect Four is a " \
    "simple game similar to Tic-Tac-Toe. \nOnly instead of three in a row, the winner must " \
    "connect four in a row. \nDue to the nature of the game setup, Connect Four is a little more "\
    "hands on and fun for younger kids to drop their checkers down the slots. \nConnect Four is a simple "\
    "and fun two player game that only takes minutes to finish. "\
    "\nObject:\nTo win Connect Four you must be the first player to get four of your colored checkers in a "\
    "row either horizontally, vertically or diagonally."




def blit_text(surface, text, pos, font, color=pygame.Color('black')):
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
    font = pygame.font.SysFont('Arial', 30)
    while True:

        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(pygame.Color('white'))
        blit_text(screen, text, (20, 20), font)
        pygame.display.update()

pygame.init()
instructions(clock, screen, text)