'''
Created on 03/05/2014

@author: Fernando
'''

import pygame
from pygame.locals import Rect
from main.util.ImageUtil import ImageUtils

SPRITE_SHEET = '1945.bmp'

#Clase que se encarga de procesar el fichero con todos los sprites,
#recuperar uno o meterlos todos en un array.
class SpriteSheet:
    
    def __init__(self, filename):
        self.sheet = ImageUtils.load_image(filename)[0]
    
    
    def imgat(self, rect, colorkey = None):
        rect = Rect(rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return ImageUtils.imgcolorkey(image, colorkey)
    
    
    def imgsat(self, rects, colorkey = None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs

#Clase que representa el fondo del juego e implementa su movimiento
class LandScape:
    speed = 2
    def __init__(self, screen):
        w = pygame.display.get_surface().get_width()
        h = pygame.display.get_surface().get_height()
        self.tileside = self.oceantile.get_height()
        self.counter = 0
        self.ocean = pygame.Surface((w, h + self.tileside)).convert()
        for x in range(w/self.tileside):
            for y in range(h/self.tileside + 1):
                self.ocean.blit(self.oceantile, (x*self.tileside, y*self.tileside))
                
                
    def scrollUp(self):
        self.counter = (self.counter - self.speed) % self.tileside
    def scrollDown(self):
        self.counter = (self.counter + self.speed) % self.tileside
        
#Manager para inicializar el fondo y su movimiento
class LandScapeManager():
    
    speed = 2
     
    def __init__(self, screen):   
        self.screen = screen
        # cargar imagenes del sprite de imagenes y asignarlas a una clase sprite
        # (hacerlo antes de que las clases sean usadas y antes de iniciar la pantalla)
        spritesheet = SpriteSheet(SPRITE_SHEET)     
        LandScape.oceantile =  spritesheet.imgat((268, 367, 32, 32))
        
        # inicializar los spritesd
        self.landScape = LandScape(screen)
        
                        
    #realiza el movimiento automatico del scroll
    def scrollLandScape(self):
            self.landScape.scrollUp()
        
    #llamar en cada iteracion del bucle de ejecucion del juego para que repinte el landscape        
    def update(self):
        self.screen.blit(self.landScape.ocean, (0, 0),
                          (0, self.landScape.counter,
                          pygame.display.get_surface().get_width(),
                          pygame.display.get_surface().get_height()))
