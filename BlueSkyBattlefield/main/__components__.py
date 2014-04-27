'''
Created on 27/04/2014

@author: Fernando
'''
import pygame
import os
from main.__utils__ import Utils

class Disparo(pygame.sprite.Sprite):
    
    def __init__(self, screen, initPosicionX, initPosicionY):
        self.screen = screen
        self.colorDisparo = (255,255,0,0)
        self.posicionX = initPosicionX
        self.posicionY = initPosicionY
        self.rectangulo = pygame.Rect((self.posicionX, self.posicionY),(5,10))
        
    def pintarDisparo(self, initPosicionX, initPosicionY):
        self.posicionX = initPosicionX
        self.posicionY = initPosicionY
        
        print(self.posicionX, self.posicionY)
        
        for i in xrange(180):
            self.posicionY = self.posicionY + 0.01
            print(self.posicionX, self.posicionY)        
            self.disparo = pygame.draw.rect(self.screen, self.colorDisparo, self.rectangulo)
            
 
class Nave(pygame.sprite.Sprite):    
       
    #screen y filename son la pantalla y la ruta del archivo que le pasamos al metodo loadImage
    #widthScale, heightScale son el reescalado del sprite , posicionX, posicionY son el lugar de la pantalla
    #en que queremos que se pinte el sprite
    def __init__(self, screen, image_dir, file_image_name, widthScale, heightScale, posicionX, posicionY):        
        self.screen = screen
        self.image = Utils.load_image(screen, image_dir, file_image_name, True)
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
        if nuevaPosicion > -2 and nuevaPosicion < self.screen.width - 21:
            self.posicionX = self.posicionX + unidades

    def moverY(self, unidades):
        self.posicionY = self.posicionX + unidades
        self.posicionY

    
class NaveHeroe(Nave):
    
    velocidadMovimiento = 15
    
    def postConstructor(self):
        self.disparos = [Disparo(self.screen, self.posicionX, self.posicionY)]
         
    def moverIzquierda(self):
        self.moverX(-self.velocidadMovimiento)
    
    def moverDerecha(self):
        self.moverX(self.velocidadMovimiento)
        
    def disparar(self):        
        print('rectx', self.image.get_rect().x)
        print('recty', self.image.get_rect().y)
        self.disparos[0].pintarDisparo(self.posicionX - self.image.get_rect().x, 0 + self.image.get_rect().y)

class NaveEnemiga(Nave):
      
    def atacar(self):
        print 'ataca al heroe'
        
        


        