from paddle import Paddle
from ball import Ball
import pygame
import numpy as np
from collections import namedtuple


# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Lab 2")
    WIDTH=800
    HEIGHT=480
    VELOCITY = 10
    BORDER = 20
    FPS = 30 # frame rate

    MyConstants = namedtuple("MyConstants",["WIDTH", "HEIGHT", "VELOCITY", "BORDER", "FPS"])
    CONSTS = MyConstants(WIDTH,HEIGHT,VELOCITY,BORDER,FPS)
    print(CONSTS.BORDER) 

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.update()
    
    #walls and color
    wcolor=pygame.Color("white")
    bgcolor = pygame.Color("black")

    
    #upper wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,0),(WIDTH,BORDER)))

    #left wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,0),(BORDER,HEIGHT)))

    #bottom wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))


    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY#randomly assign a value between + and - VELOCITY
    vy0 = np.random.randint(-VELOCITY,VELOCITY)# randomly assign a value between + and - VELOCITY
    #TODO: +/- 45 degree/random
        # constantly check to see if we are colliding with the walls borders, then flip the
        # velocity

    b0 = Ball(x0,y0, vx0, vy0, screen, wcolor, bgcolor, CONSTS)
    b0.show(wcolor)




    pygame.display.update()
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)

            #Ball
        b0.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

# TODO: push lab3 to git + capture a gif, and upload it to github in your README.md
# GIF: shows collision with the wall and the random start