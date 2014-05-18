'''
Created on 03/05/2014

@author: Fernando
'''

import pygame
from main.util.ImageUtil import ImageUtils

class LandScapeManager():
    
    def __init__(self, screen):
        print('lanscape manager')
        self.screen = screen

    def setLandScape(self, screen, imageDir, backgroundImage):
        self.background =  ImageUtils.load_image(screen, imageDir, backgroundImage)[0]
        background_size = self.background.get_size()
        background_rect = self.background.get_rect()
        #self.screen = pygame.display.set_mode(background_size)
        self.x = 0
        self.y = 0
        self.w, self.h = background_size
        
    def scrollLandScape(self):
        if(self.y > self.h):
            self.y = 0
        else:
            self.y += 5
        
        
    def update(self):
        self.screen.blit(self.background,(self.x,self.y))