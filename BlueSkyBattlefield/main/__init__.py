#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports de modulos
import pygame
from pygame.locals import*
import sys
import os

from main.__utils__ import  Utils
from main.__components__ import *
from unittest.test.test_result import __init__


# Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMAGE_DIR = "imx"


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
        if(keys[pygame.K_SPACE]):
            naveHeroe.disparar()
        
        if naveHeroe.disparando == True:
            naveHeroe.updateDisparos()
        
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
    background_image = Utils.load_image(screen, IMAGE_DIR, 'stars_blue.png')
    
    #creacion de objetos nave del protagonista
    naveHeroe = NaveHeroe(screen, IMAGE_DIR, 'spaceShip_40.png', 'lasser.png', 25, 35, ((SCREEN_WIDTH / 2) - 20), (SCREEN_HEIGHT - 65))
    
    bucleDeEjecucion()


