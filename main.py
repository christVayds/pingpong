import pygame
from player import *

pygame.init()

windowSize = (700, 500)
screen = pygame.display.set_mode((windowSize[0], windowSize[1]))
pygame.display.set_caption('pingpong game')

clock = pygame.time.Clock()
fps = 30

# players
player1 = Player(0, 0, 10, 50, 'player1')
player2 = Player(windowSize[0]-10, 0, 10, 50, 'player2')

# ball
ball = Ball(0, 250, 15, 15)

# text
text = pygame.font.SysFont('comicsansms', 20)

def draw():

    screen.fill((54, 54, 54))
    p1score = text.render(f'Player1: {player1.score}', True, (255,255,255))
    p2score = text.render(f'Player2: {player2.score}', True, (255,255,255))

    screen.blit(p1score, (10, 10, p1score.get_width(), p1score.get_height()))
    screen.blit(p2score, ((700 - p2score.get_width()), 10, p2score.get_width(), p2score.get_height()))

    # draw player
    player1.draw(screen)
    player2.draw(screen)

    # draw ball
    ball.draw(screen)
    ball.colplayer2(player2, player1)
    ball.colplayer1(player1, player2)

    pygame.display.flip()

def main():

    run = True
    while run:

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()

    pygame.quit()

if __name__=='__main__':
    main()