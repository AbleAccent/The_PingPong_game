from pygame import *
import random
from time import time as timer



window = display.set_mode((700, 500))
display.set_caption('PingPong')


class GameSprite(sprite.Sprite):
    def __init__(self, image_file, speed, x_cor, y_cor, height, widgth):
        super().__init__()
        # self.image = transform.scale(image.load(image_file), (widgth, height))
        self.speed = speed
        self.image = Surface((height, widgth))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor
        self.direction = 'left'
        self.v_direction = 'down'
    # sprite showing
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < 400:
            self.rect.y += self.speed


class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < 400:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, image_file, speed, x_cor, y_cor, height, widgth):
        super().__init__(image_file, speed, x_cor, y_cor, height, widgth)
        self.speed_x = speed
        self.speed_y = speed
        self.radius = 25
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if (self.rect.y < 0) or (self.rect.y > 490):
            self.speed_y *= -1
    
    def character(self):
        self.player_character = pygame.draw.circle(self.x_cor, self.y_cor, self.radius, self.width)

        


# background
background_color = (0, 0, 0)
background = Surface((700,500))
background.fill(background_color)


clock = time.Clock()
game = True
finish = False
FPS = 30
lost_counter = 0
kill_counter = 0

font.init()
font = font.SysFont('Arial', 30)

p1_lose = font.render('Player 1 lose!', True, (255, 0, 0))
p2_lose = font.render('Player 2 lose!', True, (255, 0, 0))

player1 = Player1('rocket.png', 15, 50, 200, 25, 100)
player2 = Player2('rocket.png', 15, 650, 200, 25, 100)
ball = Ball('ball.png', 5, 200, 200, 25, 25)



while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
            
    if finish != True:
        window.blit(background, (0, 0))

        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()

        if sprite.collide_rect(ball, player1):
            ball.speed_x *= -1
        
        if sprite.collide_rect(ball, player2):
            ball.speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(p1_lose, (350, 250))

        if ball.rect.x > 700:
            finish = True
            window.blit(p2_lose, (350, 250))

    display.update()
    clock.tick(FPS)


