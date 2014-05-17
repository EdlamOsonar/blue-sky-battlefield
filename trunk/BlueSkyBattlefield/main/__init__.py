#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports de modulos
import os
import sys

import pygame


from pygame.locals import*
from main.component.NaveHeroe import *
from main.component.NaveEnemiga import *
from main.util.ImageUtil import ImageUtils
from main.manager.ColisionManager import ColisionManager
from main.manager.ComponentManager import ComponentManager


# Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMAGE_DIR = "../resources/imx"


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
        naveHeroe.pintar()
        naveEnemiga.pintar()
             
        #movimiento de la nave del heroe
        keys=pygame.key.get_pressed()   
        if (keys[pygame.K_a])or (keys[pygame.K_LEFT]):#move left
            naveHeroe.moverIzquierda()
        if(keys[pygame.K_d]) or (keys[pygame.K_RIGHT]):#move right
            naveHeroe.moverDerecha()
        if(keys[pygame.K_SPACE]):
            naveHeroe.disparar()
        
        naveHeroe.updateDisparos()
        
        componentManager.colisionManager.execute()
        #=======================================================================
        # #detectar colisiones
        # for i in range(10):
        #     if(len(naveHeroe.arrayDisparos) >= i + 1):
        #         disparo = naveHeroe.arrayDisparos[i]
        #         #disparo.rect.y = 250
        #         print(' disparo y ' + str(disparo.rect.y) + ' disparo x ' + str(disparo.rect.x))
        #         print(' nave enemiga y ' + str(naveEnemiga.rect.y) + ' nave enemiga x ' + str(naveEnemiga.rect.x))
        #         impactoAlEnemigo = naveEnemiga.rect.colliderect(disparo.rect)                
        #         if impactoAlEnemigo:                    
        #             naveEnemiga.impacto()
        #=======================================================================
                    #disparo.destruir()
        
        #establecer velocidad de reloj y actualizar el display
        reloj.tick(30)
        pygame.display.flip()
        
    pygame.quit()

# Inicializacion(punto de entrada de la ejecucion del programa)---------------------------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN, 32)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Blue Sky Battlefield")
    pygame.mouse.set_visible(False)
    #load images
    background_image = ImageUtils.load_image(screen, IMAGE_DIR, 'stars_blue.png')[0]

    #managers
    componentManager = ComponentManager()

    #creacion de objetos nave del protagonista
    naveHeroe = componentManager.createNaveHeroe(screen, 'spaceShip_40.png', 'lasser.png', 25, 35, ((SCREEN_WIDTH / 2) - 20), (SCREEN_HEIGHT - 65))
    
    #prueba nave enemiga
    naveEnemiga = componentManager.createNaveEnemiga(screen,   'spaceShip_40.png', 'lasser.png', 25, 35, ((SCREEN_WIDTH / 2) - 20), (SCREEN_HEIGHT - 400))
    
    #bucle de ejecucion del juego
    bucleDeEjecucion()


