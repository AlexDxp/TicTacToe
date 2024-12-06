import pygame
from pygame import MOUSEBUTTONDOWN
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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
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



