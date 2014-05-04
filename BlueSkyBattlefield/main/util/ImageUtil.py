'''
Created on 27/04/2014

@author: Fernando
'''
import os

import pygame


class ImageUtils():
    
    @staticmethod
    def load_image(screen, image_dir , filename, transparent=False):
        # Encontramos la ruta completa de la imagen
        ruta = os.path.join(image_dir, filename)
        print ruta
        try:
            image = pygame.image.load(ruta)
        except pygame.error, message:
            raise  SystemExit(message)
    
        if transparent:
            image = image.convert_alpha()
        else:
            image = image.convert()
    
        return image, image.get_rect()
    
    @staticmethod
    def checkCollision(sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col 
            