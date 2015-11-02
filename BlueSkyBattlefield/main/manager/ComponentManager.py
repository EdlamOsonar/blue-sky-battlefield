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
from main.util.Constants import *
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
        
    def createNaveHeroe(self, screen, posicionX, posicionY):        
        sprite_rect_nave_heroe = [(40, 0, 45, 40),
                                  (0, 0, 40, 40),
                                  (83, 0, 40, 40),
                                  (40, 40, 45, 40),
                                  (0, 40, 40, 40),
                                  (83, 40, 40, 40)]
        imagen_disparo = 'lasser.png'
        naveHeroe = NaveHeroe(screen, sprite_rect_nave_heroe, imagen_disparo, 40, 40, posicionX, posicionY)
        naveHeroe.spriteSheet = self.spriteSheet
        naveHeroe.setColisionManager(self.colisionManager)
        self.colisionManager.add(naveHeroe)
        self.components.add(naveHeroe)
        return naveHeroe
    
    def createNaveEnemiga(self, screen, posicionX, posicionY, rutina_movimiento):
        sprite_rect_nave_enemiga = [(59, 261, 32, 32)]
        imagen_disparo = 'lasser.png'
        naveEnemiga = NaveEnemiga(screen, sprite_rect_nave_enemiga, imagen_disparo, 32, 32, posicionX, posicionY)
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
        enemie = self.createNaveEnemiga(self.screen, posicionX, 10, RUTINA_DIAGONAL)        
        #enemie = self.createNaveEnemiga(self.screen,   'rd2.png', 'lasser.png', 25, 25, posicionX, 10, RUTINA_DIAGONAL)
        #  enemie = self.componentManager.createNaveEnemiga(self.screen,   'rd2.png', 'lasser.png', 25, 25, ((self.screenWidth / 2) - 20), (self.screenHeight - 400), RUTINA_RECTO)
        enemie.velocidad = velocidadJuego
        enemie.vidas = vidas
        enemies.add(enemie)
       
        
    #Crea una rutina de dos enemigos que avanzan en paralelo hacia abajo
    #desde cada extremo de la pantalla    
    def rutinaEnemigosEnParalelo(self, enemies, vidas):
        enemie1 = ComponentManager.createNaveEnemiga(self, self.screen, 50, 10,  RUTINA_RECTO)
        enemie1.vidas = vidas
        enemies.add(enemie1)        
        enemie2 = ComponentManager.createNaveEnemiga(self, self.screen, pygame.display.get_surface().get_width() - 50, 10, RUTINA_RECTO)
        enemie2.vida = vidas
        enemies.add(enemie2)