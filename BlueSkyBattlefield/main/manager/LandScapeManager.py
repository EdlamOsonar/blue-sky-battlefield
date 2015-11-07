'''
Created on 03/05/2014

@author: Fernando
'''

import pygame
from main.util.ImageUtil import SpriteSheet, ImageUtils
from main.util.ImageUtil import SPRITE_SHEET

#Clase que representa el fondo del juego e implementa su movimiento
class LandScape:
    speed = 2
    
    
    def __init__(self, screen):
        w = pygame.display.get_surface().get_width()
        h = pygame.display.get_surface().get_height()
        self.counter = 0

        self.background = pygame.Surface((w, h + self.background_image.get_height())).convert()
        self.background.blit(self.background_image, (640, 480))
        
        self.tileside = self.scroll_tile.height
        self.scroll = pygame.Surface((w, h)).convert()
        for x in range(w/self.tileside):
            for y in range(h/self.tileside + 1):
                self.scroll.blit(self.scroll_tile, (x*self.tileside, y*self.tileside))
                
                
    def scrollUp(self):
        self.counter = (self.counter - self.speed) % self.tileside
        #print 'tileside' + str(self.tileside)
        #print 'counter ' + str(self.counter)
        
    def scrollDown(self):
        self.counter = (self.counter + self.speed) % self.tileside
        print  str(self.counter)
        
#Manager para inicializar el fondo y su movimiento
class LandScapeManager():
    
    speed = 2
     
    def __init__(self, screen):   
        self.screen = screen
        
        # cargar imagenes del sprite de imagenes y asignarlas a una clase sprite
        # (hacerlo antes de que las clases sean usadas y antes de iniciar la pantalla)       
        #cargar la imagen de fondo fija que no hace scroll
        image_background = SpriteSheet('stars_blue.png')
        LandScape.background_image = image_background.imgat((0, 0, 640, 480))
        
        self.star_imaxe = ImageUtils.load_image_transparent('big_stars_scroll.png')
        LandScape.scroll_tile =  self.star_imaxe.get_rect()
        
        # inicializar los spritesd
        self.landScape = LandScape(screen)
        self.landScape.counter = 1
        
        self.update(False)
                       
    #realiza el movimiento automatico del scroll
    def scrollLandScape(self):
        self.landScape.scrollUp()
 
        
    #llamar en cada iteracion del bucle de ejecucion del juego para que repinte el landscape        
    def update(self, in_execute):
        surface = pygame.display.get_surface()
        
        self.screen.blit(self.landScape.background_image, (0, 0),
            (0, 0, pygame.display.get_surface().get_width(),
            pygame.display.get_surface().get_height()))
        
        if(in_execute):
            self.screen.blit(self.star_imaxe, (0, 40),
                             (0, self.landScape.counter, surface.get_width(), self.star_imaxe.get_rect().height))
      