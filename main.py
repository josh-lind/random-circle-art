from random import random
import math
import arcade

class Circle:
    FLIP_ODDS = .01
    RADS_PER_CYCLE = .1
    RADIUS = .05
    
    def __init__(self, x, y, rx, ry, clockwise):
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.cw = clockwise # 1 for clockwise, -1 for ccw
        
    def rotate(self):
        theta = math.atan2(self.y-self.ry, self.x-self.rx)
        r = math.sqrt((self.x-self.rx)**2 + (self.y-self.ry)**2)
        theta += Circle.RADS_PER_CYCLE * self.cw
        self.x = self.rx + math.cos(theta)*r
        self.y = self.ry + math.sin(theta)*r
        
    def try_flip(self):
        if random() < Circle.FLIP_ODDS:
            theta = 2*pi*random()
            r = random()*Circle.RADIUS
            self.rx = self.x + cos(theta)*r
            self.ry = self.y + sin(theta)*r
            self.cw = not self.cw

class Drawing:
    def __init__(self):
        self.circles = []
        self.test = Circle(.5, .5, .51, .51, 1)
        
    def render(self):
        print(self.test.x)

    def next_state(self):
        self.test.rotate()
        self.render()

d = Drawing()
d.render()
d.next_state()

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
