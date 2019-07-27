import pygame

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe Game!')

clock = pygame.time.Clock()

colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)

board_rows = pygame.image.load('board_rows.png')
board_columns = pygame.image.load('board_columns.png')
X = pygame.image.load('X.png')
O = pygame.image.load('O.png')

status = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

game_ended = False
game_aborted = False
turn = 'X'
played_turns = 0
while not game_aborted:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_aborted = True
        if event.type == pygame.MOUSEBUTTONDOWN and not game_ended:
            pos = event.pos

            row = int(pos[0]/200)
            col = int(pos[1]/200)
            if status[row][col] == 0:
                status[row][col] = turn
                turn = 'X' if turn == 'O' else 'O'
                played_turns += 1
    screen.fill(colorWhite)
    for i in range(1,3):
        screen.blit(board_columns, (i*200, 0))
        screen.blit(board_rows, (0, i*200))
    for row in range(3):
        for col in range(3):
            pic = X if status[row][col] == 'X' else \
                  O if status[row][col] == 'O' else 0
            if pic:
                screen.blit(pic, (row*200, col*200))

    if played_turns == 9:
        game_ended = True

    pygame.display.update()
    clock.tick(60)
pass
