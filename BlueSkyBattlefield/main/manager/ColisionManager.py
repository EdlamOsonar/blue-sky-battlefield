'''
Created on 03/05/2014

@author: Fernando
'''
import pygame
from main.component.Disparo import Disparo
from main.component.NaveHeroe import NaveHeroe
from main.component.DisparoHeroe import DisparoHeroe
from main.component import DisparoEnemigo
from main.component.NaveEnemiga import NaveEnemiga


class ColisionManager(object):

    def __init__(self):
        self.arrayObjetos = []
    
    # anade un objeto al array de colisiones para ser mantenido por el ColissionManager
    def add(self, item):
            self.arrayObjetos.append(item)
    
    # elimina un objeto al array de colisiones para ser mantenido por el ColissionManager    
    def remove(self, objeto):
        if self.arrayObjetos:
            indexToRemove = -1
            for i in range(len(self.arrayObjetos) - 1):
                if self.arrayObjetos[i] == objeto:
                    indexToRemove = i
            if indexToRemove >= 0:
                self.arrayObjetos.pop(indexToRemove)
    
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
        if self.arrayObjetos:  
            for i in xrange(len(self.arrayObjetos) - 1):
                objeto1 = self.arrayObjetos[i]
                for i in xrange(len(self.arrayObjetos) - 1):
                    objeto2 = self.arrayObjetos[i]
                    if objeto1 != objeto2:                        
                        colision = self.checkCollision(objeto1, objeto2) 
                        if colision:
                            objeto1.colision()
                            objeto2.colision()
                            
    
