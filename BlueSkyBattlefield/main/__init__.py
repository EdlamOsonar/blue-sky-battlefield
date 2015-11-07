#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports de modulos
import os
import sys

import pygame

from main.component.NaveEnemiga import *
from main.component.NaveHeroe import *
from main.manager.ColisionManager import ColisionManager
from main.manager.ComponentManager import ComponentManager
from main.manager.LevelManager import LevelManager
from main.util.ImageUtil import ImageUtils


from pygame.locals import*
from main.manager.LandScapeManager import LandScapeManager


# Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMAGE_DIR = "../resources/imx"
SOUNDS_DIR = "../resources/sounds"


#Ejecucion del juego--------------------------------------------------------------------------

def bucleDeEjecucion():
   
    #Bucle principal del juego
    salir = False    
    reloj = pygame.time.Clock();
    
    while salir != True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir = True
        
        if levelManager.inExecute:
            componentManager.landScapeManager.scrollLandScape()
        componentManager.landScapeManager.update(levelManager.inExecute)
        
        levelManager.execute()
        
        componentManager.colisionManager.execute()
        componentManager.checkRemove()        
    
        
        #establecer velocidad de reloj y actualizar el display
        reloj.tick(30)
        pygame.display.update()
        pygame.display.flip()
             
    pygame.quit()

# Inicializacion(punto de entrada de la ejecucion del programa)---------------------------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN, 32)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Blue Sky Battlefield")
    pygame.mouse.set_visible(False)
    #load images
    #background_image = ImageUtils.load_image(screen, IMAGE_DIR, 'stars_blue.png')[0]
    
    
    #managers
    componentManager = ComponentManager(screen)
    levelManager = LevelManager(screen, componentManager)    
    
    #bucle de ejecucion del juego
    bucleDeEjecucion()


