'''
Created on 27/04/2014

@author: Fernando
'''
import os

import pygame

IMAGE_PATH = "../resources/imx"

class ImageUtils():
    
    @staticmethod
    def imgcolorkey(image, colorkey):
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
                #establecer el nivel de transparencia de la imagen
                image.set_colorkey(colorkey, pygame.constants.RLEACCEL)
        return image    
    
    @staticmethod
    def load_image(filename, colorkey = None, transparent = False):
        filename = os.path.join(IMAGE_PATH, filename)
            
        image = pygame.image.load(filename)
           
        if transparent:
            image = image.convert_alpha()
        else:
            image = image.convert()
            
        return ImageUtils.imgcolorkey(image, colorkey), image.get_rect() 

    
    #===========================================================================
    # @staticmethod
    # def load_image(screen, filename, transparent=False):
    #     # Encontramos la ruta completa de la imagen
    #     ruta = os.path.join(IMAGE_PATH, filename)
    #     print ruta
    #     try:
    #         image = pygame.image.load(ruta)
    #     except pygame.error, message:
    #         raise  SystemExit(message)
    # 
    #     if transparent:
    #         image = image.convert_alpha()
    #     else:
    #         image = image.convert()
    # 
    #     return image, image.get_rect()
    #===========================================================================
    
    @staticmethod
    def checkCollision(sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col 
            