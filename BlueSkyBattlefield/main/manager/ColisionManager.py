'''
Created on 03/05/2014

@author: Fernando
'''
import pygame

from main.component import DisparoEnemigo
from main.component.Disparo import Disparo
from main.component.DisparoHeroe import DisparoHeroe
from main.component.NaveEnemiga import NaveEnemiga
from main.component.NaveHeroe import NaveHeroe


class ColisionManager(object):

    def __init__(self):
        self.objetos = pygame.sprite.Group()
    
    # anade un objeto al array de colisiones para ser mantenido por el ColissionManager
    def add(self, item):
            self.objetos.add(item)
    
    # elimina un objeto al array de colisiones para ser mantenido por el ColissionManager    
    def remove(self, objeto):
        self.objetos.remove(objeto)
    
    #comprueba si se ha producido colision entre dos sprites       
    def checkCollision(self, sprite1, sprite2):
        
        #validar que no son el mismo tipo de objetos y que por tanto no pueden colisionar
        ambosSpritesSonDisparo = type(sprite1) is Disparo and type(sprite2) is Disparo
        ambosSpritesSonDisparoHeroe = type(sprite1) is DisparoHeroe and type(sprite2) is DisparoHeroe
        ambosSpritesSonDisparoEnemigo = type(sprite1) is DisparoEnemigo and type(sprite2) is DisparoEnemigo
        naveHeroeAndDisparoHeroe = type(sprite1) is DisparoHeroe and type(sprite2) is NaveHeroe
        disparoHeroeAndNaveHeroe = type(sprite2) is DisparoHeroe and type(sprite1) is NaveHeroe
        naveEnemigaAndDisparoEnemigo = type(sprite1) is DisparoEnemigo and type(sprite2) is NaveEnemiga
        disparoEnemigoAndNaveEnemigo = type(sprite2) is DisparoEnemigo and type(sprite1) is NaveEnemiga
        
        #comprobar la colision
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        
        #condicion para que exista colision
        return (col and (ambosSpritesSonDisparo == False) and (naveHeroeAndDisparoHeroe == False) 
            and (disparoHeroeAndNaveHeroe == False) and (naveEnemigaAndDisparoEnemigo == False) 
            and (disparoEnemigoAndNaveEnemigo == False) and (ambosSpritesSonDisparoEnemigo == False)
            and (ambosSpritesSonDisparoHeroe == False))
    
    # recorre el array de colisiones comprobando que los objetos colisionen, si colisionan lo notifica
    def execute(self):
        componentes = self.objetos.sprites()
        if componentes:  
            componentesLen = len(componentes) - 1
            for index1 in xrange(componentesLen):
                objeto1 = self.objetos.sprites()[index1]
                for index2 in xrange(componentesLen):
                    objeto2 = self.objetos.sprites()[index2]
                    if objeto1 != objeto2:                        
                        colision = self.checkCollision(objeto1, objeto2) 
                        if colision:
                            objeto1.colision()
                            objeto2.colision()
                            
    
