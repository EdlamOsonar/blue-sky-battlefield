'''
Created on 04/05/2014

@author: Fernando
'''
from main.component.Disparo import Disparo
from main.manager.ColisionManager import ColisionManager

class ComponentFactory(object):
    '''
    classdocs
    '''


    def __init__(self, colisionManager):
        self.colisionManager = ColisionManager()
        
    @staticmethod
    def createDisparo(self, screen, imageDir, imageFileName, width, height, arrayDisparos):
            disparo = Disparo(screen, imageDir, imageFileName, width, height)
            disparo.posicionX = self.posicionX + self.width / 2
            disparo.posicionY = self.posicionY
            arrayDisparos.append(disparo)                    
            self.colisionManager.add(disparo)