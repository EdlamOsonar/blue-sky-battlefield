'''
Created on 27/04/2014

@author: Fernando
'''
import pygame
import os
from main.__utils__ import Utils


            
 
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
        self.disparando = False
        self.disparos = [Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5)]
         
    def moverIzquierda(self):
        self.moverX(-self.velocidadMovimiento)
    
    def moverDerecha(self):
        self.moverX(self.velocidadMovimiento)
        
    def disparar(self):        
        self.disparando = True
        for i in xrange(len(self.disparos)):
            self.disparos[i].pintar(self.posicionX , self.posicionY)
    
    def updateDisparos(self):
        for i in xrange(len(self.disparos)):
            self.disparos[i].update()

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
        
    def pintar(self, initPosicionX, initPosicionY):
        self.posicionX = initPosicionX
        self.posicionY = initPosicionY
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
    
    def update(self):
        self.posicionY = self.posicionY -10
        self.screen.blit(self.scaledImage, (self.posicionX + 5, self.posicionY - 10))
            
        