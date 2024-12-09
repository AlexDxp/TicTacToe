import pygame
from pygame import MOUSEBUTTONDOWN
import sys
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = 200
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TicTacToe")
screen.fill(pygame.Color(WHITE))
turn = 0
TopRow = ['#'] * 3
MidRow = ['#'] * 3
BotRow = ['#'] * 3
for i in range(9):
    if i == 0:
        x = 0
        y = 0
    if i == 1:
        x = 200
        y = 0
    if i == 2:
        x = 400
        y = 0
    if i == 3:
        x = 0
        y = 200
    if i == 4:
        x = 200
        y = 200
    if i == 5:
        x = 400
        y = 200
    if i == 6:
        x = 0
        y = 400
    if i == 7:
        x = 200
        y = 400
    if i == 8:
        x = 400
        y = 400
    rect = pygame.Rect(x, y, size, size)
    gridlines = pygame.draw.rect(screen, BLACK, rect, 1)
pygame.display.flip()
X = pygame.image.load("Images/198x198 X.png")
O = pygame.image.load("Images/198x198 O.png")
Xwin = pygame.image.load("Images/X win.png")
Owin = pygame.image.load("Images/O win.png")
Tie = pygame.image.load("Images/Tie.png")
win = '#'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                if 0 <= x < 200 and 0 <= y < 200:
                    go = TopRow[0]
                elif 0 <= x <= 200 and 200 <= y <= 400:
                    go = MidRow[0]
                elif 0 <= x < 200 and 400 <= y <= 600:
                    go = BotRow[0]
                elif 200 <= x < 400 and 0 <= y <= 200:
                    go = TopRow[1]
                elif 200 <= x < 400 and 200 <= y <= 400:
                    go = MidRow[1]
                elif 200 <= x < 400 and 400 <= y <= 600:
                    go = BotRow[1]
                elif 400 <= x < 600 and 0 <= y <= 200:
                    go = TopRow[2]
                elif 400 <= x < 600 and 200 <= y <= 400:
                    go = MidRow[2]
                elif 400 <= x < 600 and 400 <= y <= 600:
                    go = BotRow[2]
                if go != '#':
                    continue
                elif go == '#':
                    if turn % 2 == 0:
                        if 0 <= x < 200 and 0 <= y < 200:
                            TopRow[0] = 'X'
                        elif 0 <= x <= 200 and 200 <= y <= 400:
                            MidRow[0] = 'X'
                        elif 0 <= x < 200 and 400 <= y <= 600:
                            BotRow[0] = 'X'
                        elif 200 <= x < 400 and 0 <= y <= 200:
                            TopRow[1] = 'X'
                        elif 200 <= x < 400 and 200 <= y <= 400:
                            MidRow[1] = 'X'
                        elif 200 <= x < 400 and 400 <= y <= 600:
                            BotRow[1] = 'X'
                        elif 400 <= x < 600 and 0 <= y <= 200:
                            TopRow[2] = 'X'
                        elif 400 <= x < 600 and 200 <= y <= 400:
                            MidRow[2] = 'X'
                        elif 400 <= x < 600 and 400 <= y <= 600:
                            BotRow[2] = 'X'
                    elif turn % 2 != 0:
                        if 0 <= x < 200 and 0 <= y < 200:
                            TopRow[0] = 'O'
                        elif 0 <= x <= 200 and 200 <= y <= 400:
                            MidRow[0] = 'O'
                        elif 0 <= x < 200 and 400 <= y <= 600:
                            BotRow[0] = 'O'
                        elif 200 <= x < 400 and 0 <= y <= 200:
                            TopRow[1] = 'O'
                        elif 200 <= x < 400 and 200 <= y <= 400:
                            MidRow[1] = 'O'
                        elif 200 <= x < 400 and 400 <= y <= 600:
                            BotRow[1] = 'O'
                        elif 400 <= x < 600 and 0 <= y <= 200:
                            TopRow[2] = 'O'
                        elif 400 <= x < 600 and 200 <= y <= 400:
                            MidRow[2] = 'O'
                        elif 400 <= x < 600 and 400 <= y <= 600:
                            BotRow[2] = 'O'
                    if turn % 2 == 0:
                        if 0 <= x < 200 and 0 <= y < 200:
                            screen.blit(X, (0, 0))
                            pygame.display.flip()
                        elif 0 <= x <= 200 and 200 <= y <= 400:
                            screen.blit(X, (0, 200))
                            pygame.display.flip()
                        elif 0 <= x < 200 and 400 <= y <= 600:
                            screen.blit(X, (0, 400))
                            pygame.display.flip()
                        elif 200 <= x < 400 and 0 <= y <= 200:
                            screen.blit(X, (200, 0))
                            pygame.display.flip()
                        elif 200 <= x < 400 and 200 <= y <= 400:
                            screen.blit(X, (200, 200))
                            pygame.display.flip()
                        elif 200 <= x < 400 and 400 <= y <= 600:
                            screen.blit(X, (200, 400))
                            pygame.display.flip()
                        elif 400 <= x < 600 and 0 <= y <= 200:
                            screen.blit(X, (400, 0))
                            pygame.display.flip()
                        elif 400 <= x < 600 and 200 <= y <= 400:
                            screen.blit(X, (400, 200))
                            pygame.display.flip()
                        elif 400 <= x < 600 and 400 <= y <= 600:
                            screen.blit(X, (400, 400))
                            pygame.display.flip()
                        turn += 1
                    elif turn % 2 != 0:
                        if 0 <= x < 200 and 0 <= y < 200:
                            screen.blit(O, (0, 0))
                            pygame.display.flip()
                        elif 0 <= x <= 200 and 200 <= y <= 400:
                            screen.blit(O, (0, 200))
                            pygame.display.flip()
                        elif 0 <= x < 200 and 400 <= y <= 600:
                            screen.blit(O, (0, 400))
                            pygame.display.flip()
                        elif 200 <= x < 400 and 0 <= y <= 200:
                            screen.blit(O, (200, 0))
                            pygame.display.flip()
                        elif 200 <= x < 400 and 200 <= y <= 400:
                            screen.blit(O, (200, 200))
                            pygame.display.flip()
                        elif 200 <= x < 400 and 400 <= y <= 600:
                            screen.blit(O, (200, 400))
                            pygame.display.flip()
                        elif 400 <= x < 600 and 0 <= y <= 200:
                            screen.blit(O, (400, 0))
                            pygame.display.flip()
                        elif 400 <= x < 600 and 200 <= y <= 400:
                            screen.blit(O, (400, 200))
                            pygame.display.flip()
                        elif 400 <= x < 600 and 400 <= y <= 600:
                            screen.blit(O, (400, 400))
                            pygame.display.flip()
                        turn += 1
                    if TopRow[0] == TopRow[1] == TopRow[2] == 'X':
                        win = 'X'
                    elif MidRow[0] == MidRow[1] == MidRow[2] == 'X':
                        win = 'X'
                    elif BotRow[0] == BotRow[1] == BotRow[2] == 'X':
                        win = 'X'
                    elif TopRow[0] == MidRow[0] == BotRow[0] == 'X':
                        win = 'X'
                    elif TopRow[1] == MidRow[1] == BotRow[1] == 'X':
                        win = 'X'
                    elif TopRow[2] == MidRow[2] == BotRow[2] == 'X':
                        win = 'X'
                    elif TopRow[0] == MidRow[1] == BotRow[2] == 'X':
                        win = 'X'
                    elif TopRow[2] == MidRow[1] == BotRow[0] == 'X':
                        win = 'X'
                    elif TopRow[0] == TopRow[1] == TopRow[2] == 'O':
                        win = 'O'
                    elif MidRow[0] == MidRow[1] == MidRow[2] == 'O':
                        win = 'O'
                    elif BotRow[0] == BotRow[1] == BotRow[2] == 'O':
                        win = 'O'
                    elif TopRow[0] == MidRow[0] == BotRow[0] == 'O':
                        win = 'O'
                    elif TopRow[1] == MidRow[1] == BotRow[1] == 'O':
                        win = 'O'
                    elif TopRow[2] == MidRow[2] == BotRow[2] == 'O':
                        win = 'O'
                    elif TopRow[0] == MidRow[1] == BotRow[2] == 'O':
                        win = 'O'
                    elif TopRow[2] == MidRow[1] == BotRow[0] == 'O':
                        win = 'O'
                    if win == 'X':
                        screen.blit(Xwin,(0, 0))
                    elif win == 'O':
                        screen.blit(Owin,(0, 0))
                    if TopRow[0] != '#' and TopRow[1] != '#' and TopRow[2] != '#' and MidRow[0] != '#' and MidRow[1] != '#' and MidRow[2] != '#' and BotRow[0] != '#' and BotRow[1] != '#' and BotRow[2] != '#':
                        screen.blit(Tie, (0, 0))
                    pygame.display.flip()