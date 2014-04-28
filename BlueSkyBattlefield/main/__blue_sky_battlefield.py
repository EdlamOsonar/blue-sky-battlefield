#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports de modulos
import pygame
from pygame.locals import*
import sys
import os

from unittest.test.test_result import __init__


# Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMAGE_DIR = "imx"

#UTILIDADES-----------------------------------------------------------------------------------

class Utils():
    
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
    
        return image
    
#CLASES--------------------------------------------------------------------------------------

class Nave(pygame.sprite.Sprite):    
       
    #screen y filename son la pantalla y la ruta del archivo que le pasamos al metodo loadImage
    #widthScale, heightScale son el reescalado del sprite , posicionX, posicionY son el lugar de la pantalla
    #en que queremos que se pinte el sprite
    def __init__(self, screen, image_dir, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY):        
        self.screen = screen
        self.image_dir = image_dir
        
        self.image = Utils.load_image(screen, image_dir, imagen, True)
        self.file_name_image_disparo = imagen_disparo
        
        self.scaledImage = pygame.transform.scale(self.image, (widthScale, heightScale))
        
        #posiciones en pantalla y tamano del objeto
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.width = widthScale
        self.height = heightScale
        
        self.postConstructor()

    def postConstrucor(self):
        pass
        
    def pintar(self):
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
        
    def moverX(self, unidades):       
        nuevaPosicion = self.posicionX + unidades
        if nuevaPosicion > -2 and nuevaPosicion < self.screen.get_width() - 21:
            self.posicionX = self.posicionX + unidades

    def moverY(self, unidades):
        self.posicionY = self.posicionX + unidades
        self.posicionY

    
class NaveHeroe(Nave):
    
    velocidadMovimiento = 15
    
    def postConstructor(self):
        self.numeroDisparos =0
        
        #crear aray de disparos
        self.disparos = [Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5)]
         
    def moverIzquierda(self):
        self.moverX(-self.velocidadMovimiento)
    
    def moverDerecha(self):
        self.moverX(self.velocidadMovimiento)
        
    def disparar(self):        
        if self.numeroDisparos < len(self.disparos):
            disparo = self.disparos[self.numeroDisparos]
            if disparo.enabled == False:                        
                disparo.pintar(self.posicionX , self.posicionY)     
                disparo.enabled = True           
                self.numeroDisparos = self.numeroDisparos + 1           
        
            
    def updateDisparos(self):
        for i in xrange(self.numeroDisparos):
            self.disparos[i].update()
            
            #comprobar si los disparos ya no estan en pantalla para disminuir el contao de disparos (solo puede haber self.numeroDisparos en pantalla)
            if self.disparos[i].posicionY < 0 and self.disparos[i].enabled == True:                
                self.disparos[i].posicionX = self.posicionX
                self.disparos[i].posicionY = self.posicionY
                self.numeroDisparos = self.numeroDisparos - 1
                self.disparos[i].enabled = False
                print("disparo -> " + str(i) + " posicion en pantalla en el eje y " + str(self.disparos[i].posicionY))

class NaveEnemiga(Nave):
      
    def atacar(self):
        print 'ataca al heroe'
        
        
class Disparo(pygame.sprite.Sprite):
    
    def __init__(self, screen, image_dir, file_image_name, widthScale, heightScale):
        self.screen = screen
        self.image = Utils.load_image(screen, image_dir, file_image_name, True)
        self.scaledImage = pygame.transform.scale(self.image, (widthScale, heightScale))
        self.posicionX = 0
        self.posicionY = 0
        self.enabled = False
        
    def pintar(self, initPosicionX, initPosicionY):        
        self.posicionX = initPosicionX
        self.posicionY = initPosicionY
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
    
    def update(self):
        if self.enabled == True:
            self.posicionY = self.posicionY -10
            self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
            
      
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
    pygame.display.set_caption("Blue Sky Battlefield")
    pygame.mouse.set_visible(False)
    #load images
    background_image = Utils.load_image(screen, IMAGE_DIR, 'stars_blue.png')
    
    #creacion de objetos nave del protagonista
    naveHeroe = NaveHeroe(screen, IMAGE_DIR, 'spaceShip_40.png', 'lasser.png', 25, 35, ((SCREEN_WIDTH / 2) - 20), (SCREEN_HEIGHT - 65))
    
    bucleDeEjecucion()


