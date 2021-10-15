import pygame
 
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
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.update()
    
    #walls
    wcolor=pygame.Color("white")
    BORDER=20
    
    #upper wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,0),(WIDTH,BORDER)))

    #left wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,0),(BORDER,HEIGHT)))

    #upper wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))

    pygame.display.update()
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()