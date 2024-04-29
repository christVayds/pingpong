import pygame
import random

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, name=''):
        super().__init__()
        self.width = width
        self.height = height
        self.name = name

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))
        
        self.speed = 15
        self.score = 0

    def draw(self, screen):

        self.movement()
        
        pygame.draw.rect(screen, (255,255,255), self.rect)

    def move(self, direction):
        self.rect.y += (self.speed * direction)

    def checkOverlap(self):
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 500-self.height:
            self.rect.y = 500-self.height

    def movement(self):

        keys = pygame.key.get_pressed()

        self.checkOverlap()

        if self.name == 'player1':
            if keys[pygame.K_w]:
                self.move(-1)
            elif keys[pygame.K_s]:
                self.move(1)
        if self.name == 'player2':
            if keys[pygame.K_UP]:
                self.move(-1)
            elif keys[pygame.K_DOWN]:
                self.move(1)

class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.width = width
        self.height = height
        
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))

        self.speed = 10
        self.y_direction = 1
        self.x_direction = 1
        self.colors = [(255,255,255), (50, 168, 82), (18, 255, 235), (179, 252, 43), (179, 252, 43), (231, 43, 252)]
        self.color = self.colors[0]

    def draw(self, screen):
        pygame.draw.rect(screen, (self.color), self.rect)

        self.checkCollision()
        self.move_x(self.x_direction)
        self.move_y(self.y_direction)

    def checkCollision(self):
        if self.rect.y < 0:
            self.y_direction = 1
        elif self.rect.y >= 480:
            self.y_direction = -1

    def colplayer2(self, player, opponent):
        if self.rect.x > player.rect.x:
            opponent.score += 1
            self.reset()

        if pygame.sprite.collide_mask(self, player):
            self.y_direction = random.choice([1,-1])
            self.x_direction = -1

    def colplayer1(self, player, oppponent):
        if self.rect.x < player.rect.x:
            oppponent.score += 1
            self.reset()
            
        if pygame.sprite.collide_mask(self, player):
            self.y_direction = random.choice([1,-1])
            self.x_direction = 1

    def move_x(self, direction):
        self.rect.x += self.speed * direction

    def move_y(self, direction):
        self.rect.y += self.speed * direction

    def reset(self):
        self.rect.x = (500 - self.width) / 2
        self.rect.y = (700 - self.height) / 2
        self.color = random.choice(self.colors)
        self.y_direction = random.choice([1, -1])
        self.x_direction = random.choice([1, -1])