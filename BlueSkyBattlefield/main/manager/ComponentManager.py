'''
Created on 04/05/2014

@author: Fernando
'''
import pygame
import random
from main.component.Disparo import Disparo
from main.component.NaveHeroe import NaveHeroe
from main.component.NaveEnemiga import NaveEnemiga
from main.manager.ColisionManager import ColisionManager
from main.manager.LandScapeManager import LandScapeManager
from main.manager.SoundManager import SoundManager
from main.util.ImageUtil import SpriteSheet
from main.util.ImageUtil import SPRITE_SHEET
from main.util.Constants import RUTINA_RECTO
from main.component.ScoreBar import ScoreBar


class ComponentManager():
    '''
    classdocs
    '''


    def __init__(self, screen):
        self.screen = screen
        self.spriteSheet = SpriteSheet(SPRITE_SHEET)
        self.colisionManager = ColisionManager()
        self.landScapeManager = LandScapeManager(screen)
        self.soundManager = SoundManager()        
        self.components = pygame.sprite.Group()
        
    
    def createDisparo(self, screen, imageFileName, width, height, arrayDisparos, parentObject):
            disparo = Disparo(screen, imageFileName, width, height, parentObject)
            disparo.posicionX = self.posicionX + self.width / 2
            disparo.posicionY = self.posicionY
            arrayDisparos.append(disparo)                    
            self.colisionManager.add(disparo)
            self.components.add(disparo)
            return disparo
        
    def createNaveHeroe(self, screen, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY):
        naveHeroe = NaveHeroe(screen, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY)
        naveHeroe.spriteSheet = self.spriteSheet
        naveHeroe.setColisionManager(self.colisionManager)
        self.colisionManager.add(naveHeroe)
        self.components.add(naveHeroe)
        return naveHeroe
    
    def createNaveEnemiga(self, screen, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY, rutina_movimiento):
        naveEnemiga = NaveEnemiga(screen, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY)
        naveEnemiga.rutina_movimiento = rutina_movimiento
        self.colisionManager.add(naveEnemiga)
        self.components.add(naveEnemiga)
        return naveEnemiga
    
    
    def checkRemove(self):
        spritesBorrar = []
        for item in self.components.sprites():
            if item.borrar:
                spritesBorrar.append(item)
        
        for item in spritesBorrar:
            self.colisionManager.remove(item)
            self.components.remove(item)
            
    def createEnemies(self, enemies, velocidadJuego, vidas):
        posicionX = random.randint(1, pygame.display.get_surface().get_width() -21)        
        enemie = self.createNaveEnemiga(self.screen,   'rd2.png', 'lasser.png', 25, 25, posicionX, 10, RUTINA_RECTO)
        #  enemie = self.componentManager.createNaveEnemiga(self.screen,   'rd2.png', 'lasser.png', 25, 25, ((self.screenWidth / 2) - 20), (self.screenHeight - 400), RUTINA_RECTO)
        enemie.velocidad = velocidadJuego
        enemie.vidas = vidas
        enemies.add(enemie)
       
        
    #Crea una rutina de dos enemigos que avanzan en paralelo hacia abajo
    #desde cada extremo de la pantalla    
    def rutinaEnemigosEnParalelo(self, enemies, vidas, imagen, imagen_disparo, widthScale, heightScale):
        enemie1 = ComponentManager.createNaveEnemiga(self, self.screen, imagen, imagen_disparo, widthScale, heightScale, 50, 10,  RUTINA_RECTO)
        enemie1.vidas = vidas
        enemies.add(enemie1)        
        enemie2 = ComponentManager.createNaveEnemiga(self, self.screen, imagen, imagen_disparo, widthScale, heightScale, pygame.display.get_surface().get_width() - 50, 10, RUTINA_RECTO)
        enemie2.vida = vidas
        enemies.add(enemie2)