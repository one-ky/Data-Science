import pygame

class Ball:
    pass
    #Class variables
    RADIUS = 10

    def __init__(self,x,y, vx, vy, screen, wcolor, bgcolor, CONSTS):
        #instance variables
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.wcolor = wcolor
        self.bgcolor = bgcolor
        self.CONSTS = CONSTS

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        #new position = old position + difference delta, vx = velocity x
        # delete old ball
        self.show(self.bgcolor)
        px = self.x + self.vx
        py = self.y + self.vy
        
        # Left wall
        if px < self.CONSTS.BORDER + self.RADIUS:
            self.vx = -self.vx
        
        # do top and bottom wall as well
        if py < (self.CONSTS.BORDER + self.RADIUS) or py>(self.CONSTS.HEIGHT -self.CONSTS.BORDER - self.RADIUS):
            self.vy = -self.vy
        
        #self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.wcolor)
        # TODO:
        # Check if I'm collision (wall position)
            # flip the velocity
        

        
    