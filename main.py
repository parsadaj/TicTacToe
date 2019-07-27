import pygame

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe Game!')

colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)

board_rows = pygame.image.load('board_rows.png')
board_columns = pygame.image.load('board_columns.png')
X = pygame.image.load('X.png')
O = pygame.image.load('O.png')

status = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

pass
