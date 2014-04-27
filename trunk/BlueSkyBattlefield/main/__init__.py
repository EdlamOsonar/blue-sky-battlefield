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
    
    #screen y filename son la pantalla y la ruta del archivo que le pasamos al metodo loadImage
    #widthScale, heightScale son el reescalado del sprite , posicionX, posicionY son el lugar de la pantalla
    #en que queremos que se pinte el sprite
    def __init__(self, screen, filename, widthScale, heightScale, posicionX, posicionY):        
        self.image = load_image(screen, filename, True)
        self.scaledImage = pygame.transform.scale(self.image, (widthScale, heightScale))
        
        #posiciones en pantalla y tamano del objeto
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.width = widthScale
        self.height = heightScale
        
    def pintar(self):
        screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
        
    def moverX(self, unidades):       
        nuevaPosicion = self.posicionX + unidades
        if nuevaPosicion > -2 and nuevaPosicion < SCREEN_WIDTH - 21:
            self.posicionX = self.posicionX + unidades

    def moverY(self, unidades):
        self.posicionY = self.posicionX + unidades
        self.posicionY

    
class NaveHeroe(Nave):
    
    velocidadMovimiento = 15
    
    def disparar(self):
        print 'disparo'
        
    def moverIzquierda(self):
        self.moverX(-self.velocidadMovimiento)
    
    def moverDerecha(self):
        self.moverX(self.velocidadMovimiento)

class NaveEnemiga(Nave):
    
    def atacar(self):
        print 'ataca al heroe'
    
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
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir = True        
        
        #set images position
        screen.blit(background_image, (0, 0))
        #screen.blit(naveHeroe.scaledImage, ((SCREEN_WIDTH / 2) - 20, SCREEN_HEIGHT - 65))
        naveHeroe.pintar()
                
        #movimiento de la nave del heroe
        keys=pygame.key.get_pressed()   
        if (keys[pygame.K_a])or (keys[pygame.K_LEFT]):#move left
            naveHeroe.moverIzquierda()
        if(keys[pygame.K_d]) or (keys[pygame.K_RIGHT]):#move right
            naveHeroe.moverDerecha()
        
        #establecer velocidad de reloj y actualizar el display
        reloj.tick(25)
        pygame.display.flip()
        
    pygame.quit()
#--------------------------------------------------------------------------

# Inicializacion(punto de entrada de la ejecucion del programa)---------------------------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN, 32)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Blue Space Battlefield")
    pygame.mouse.set_visible(False)
    #load images
    background_image = load_image(screen, 'stars_blue.png')
    
    #creacion de objetos nave del protagonista
    naveHeroe = NaveHeroe(screen, 'spaceShip_40.png', 25, 35, ((SCREEN_WIDTH / 2) - 20), (SCREEN_HEIGHT - 65))

    bucleDeEjecucion()


