from pygame import *
import random
from time import time as timer


window = display.set_mode((700, 500))
display.set_caption('PingPong')


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


while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
        

            
    if finish != True:
        window.blit(background, (0, 0))


    display.update()
    clock.tick(FPS)


