'''
Created on 03/05/2014

@author: Fernando
'''
import pygame


class ColisionManager(object):

    def __init__(self):
        self.arrayObjetos = []
    
        # anade un objeto al array de colisiones para ser mantenido por el ColissionManager
    def add(self, item):
            self.arrayObjetos.append(item)
    
    
    def remove(self, objeto):
        if self.arrayObjetos:
            indexToRemove = -1
            for i in range(len(self.arrayObjetos) - 1):
                if self.arrayObjetos[i] == objeto:
                    indexToRemove = i
            if indexToRemove >= 0:
                self.arrayObjetos.pop(indexToRemove)
                    
    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col 
    
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
                            objeto1.posicionX = objeto1.posicionX - 10
    
