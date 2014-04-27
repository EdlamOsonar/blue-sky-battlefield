#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports de modulos
import pygame
from pygame.locals import*
import sys
import os
from main.__test__ import Nave


# Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMAGE_DIR = "imx"


# Clases--------------------------------------------------------------

class Nave(pygame.sprite.Sprite):
        
    def __init__(self, screen, filename, widthScale, heightScale):        
        print("Se instancia una nueva imagen")
        self.image = load_image(screen, filename, True)
        self.scaledImage = pygame.transform.scale(self.image, (widthScale, heightScale))
        
    def getImage(self):
        return self.image
    
    def getScaledImage(self):
        return self.scaledImage
        

# ---------------------------------------------------------------------

# Funciones------------------------------------------------------------

def load_image(screen, filename, transparent=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(IMAGE_DIR, filename)
    print ruta
    try:
        image = pygame.image.load(ruta)
    except pygame.error, message:
        raise  SystemExit(message)

    if transparent:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image

#Ejecucion del juego--------------------------------------------------------------------------

def bucleDeEjecucion():
   
    #Bucle principal del juego
    salir = False    
    reloj = pygame.time.Clock();
    while salir != True:
        #set images position
        screen.blit(background_image, (0, 0))
        screen.blit(naveHeroe.getScaledImage(), ((SCREEN_WIDTH / 2) - 20, SCREEN_HEIGHT - 65))
        
        for evento in pygame.event.get():
            #movimiento de la nave
            if evento.type == pygame.K_LEFT:
                print "move left"
            if evento.type == pygame.K_RIGHT:
                print "move right"
            if evento.type == QUIT:
                salir = True
        reloj.tick(25)
        pygame.display.flip()
    pygame.quit()
#--------------------------------------------------------------------------

# Inicializacion(punto de entrada de la ejecucion del programa)---------------------------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Blue Space Battlefield")

    #load images
    background_image = load_image(screen, 'stars_blue.png')
    
    #creacion de objetos nave del protagonista
    naveHeroe = Nave(screen, 'spaceShip_40.png', 25, 35)

    bucleDeEjecucion()


