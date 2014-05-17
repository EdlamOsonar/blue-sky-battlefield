'''
Created on 04/05/2014

@author: Fernando
'''
from main.component.Disparo import Disparo
from main.component.NaveHeroe import NaveHeroe
from main.manager.ColisionManager import ColisionManager
from main.manager.LandScapeManager import LandScapeManager
from main.component.NaveEnemiga import NaveEnemiga


class ComponentManager():
    '''
    classdocs
    '''


    def __init__(self):
        self.colisionManager = ColisionManager()
        self.landScapeManager = LandScapeManager()
        
    
    def createDisparo(self, screen, imageFileName, width, height, arrayDisparos):
            disparo = Disparo(screen, "../resources/imx", imageFileName, width, height)
            disparo.posicionX = self.posicionX + self.width / 2
            disparo.posicionY = self.posicionY
            arrayDisparos.append(disparo)                    
            self.colisionManager.add(disparo)
            return disparo
        
    def createNaveHeroe(self, screen, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY):
        naveHeroe = NaveHeroe(screen, "../resources/imx", imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY)
        naveHeroe.setColisionManager(self.colisionManager)
        self.colisionManager.add(naveHeroe)
        return naveHeroe
    
    def createNaveEnemiga(self, screen, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY):
        naveEnemiga = NaveEnemiga(screen, "../resources/imx", imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY)
        self.colisionManager.add(naveEnemiga)
        return naveEnemiga