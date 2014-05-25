'''
Created on 04/05/2014

@author: Fernando
'''
import pygame

from main.component.Disparo import Disparo
from main.component.NaveHeroe import NaveHeroe
from main.component.NaveEnemiga import NaveEnemiga
from main.manager.ColisionManager import ColisionManager
from main.manager.LandScapeManager import LandScapeManager
from main.manager.SoundManager import SoundManager
from main.util.ImageUtil import SpriteSheet
from main.util.ImageUtil import SPRITE_SHEET

class ComponentManager():
    '''
    classdocs
    '''


    def __init__(self, screen):
        self.spriteSheet = SpriteSheet(SPRITE_SHEET)
        self.colisionManager = ColisionManager()
        self.landScapeManager = LandScapeManager(screen)
        self.soundManager = SoundManager()        
        self.components = pygame.sprite.Group()
        
    
    def createDisparo(self, screen, imageFileName, width, height, arrayDisparos):
            disparo = Disparo(screen, imageFileName, width, height)
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
    
    def createNaveEnemiga(self, screen, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY):
        naveEnemiga = NaveEnemiga(screen, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY)
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