'''
Created on 03/05/2014

@author: Fernando
'''

import os, pygame
from pygame.locals import *
from main.util.ImageUtil import ImageUtils

# game constants
SCREENRECT = Rect(0, 0, 640, 480)

def imgcolorkey(image, colorkey):
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

def load_image(filename, colorkey = None):
    filename = os.path.join('../resources/imx/', filename)
    image = pygame.image.load(filename).convert()
    return imgcolorkey(image, colorkey)

class SpriteSheet:
    def __init__(self, filename):
        self.sheet = load_image(filename)
    def imgat(self, rect, colorkey = None):
        rect = Rect(rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return imgcolorkey(image, colorkey)
    def imgsat(self, rects, colorkey = None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs

class Arena:
    speed = 2
    def __init__(self):
        w = SCREENRECT.width
        h = SCREENRECT.height
        self.tileside = self.oceantile.get_height()
        self.counter = 0
        self.ocean = pygame.Surface((w, h + self.tileside)).convert()
        for x in range(w/self.tileside):
            for y in range(h/self.tileside + 1):
                self.ocean.blit(self.oceantile, (x*self.tileside, y*self.tileside))
    def increment(self):
        self.counter = (self.counter - self.speed) % self.tileside
    def decrement(self):
        self.counter = (self.counter + self.speed) % self.tileside
        
class LandScapeManager():
    
    speed = 2
     
    def __init__(self, screen):   
        self.screen = screen
        # load images, assign to sprite classes
        # (do this before the classes are used, after screen setup)
        spritesheet = SpriteSheet('1945.bmp')     
        Arena.oceantile =  spritesheet.imgat((268, 367, 32, 32))
        # load images, assign to sprite classes
        # (do this before the classes are used, after screen setup)
        spritesheet = SpriteSheet('1945.bmp')
        
        # initialize our starting sprites
        self.arena = Arena()
        
                
    
    def increment(self):
        self.counter = (self.counter - self.speed) % self.tileside
    
    def decrement(self):
        self.counter = (self.counter + self.speed) % self.tileside

        
    def scrollLandScape(self):
            self.arena.increment()
        
        
    def update(self):
        self.screen.blit(self.arena.ocean, (0, 0), (0, self.arena.counter, SCREENRECT.width, SCREENRECT.height))
