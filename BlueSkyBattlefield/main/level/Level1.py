'''
Created on 3/11/2014

@author: Fernando
'''
import pygame
from main.util.SoundUtil import SoundUtil
from main.manager.LevelState import LevelState

class Level1(LevelState):
    '''
    classdocs
    '''


    def __init__(self, screen, componentManager):
        '''
        Constructor
        '''
        
        self.screen = screen
        self.componentManager = componentManager
        self.screenWidth = pygame.display.get_surface().get_width()
        self.screenHeight = pygame.display.get_surface().get_height()
        
        self.resetAtributosGlobales()
        self.resetLevelAtributes()
        
    def resetLevelAtributes(self):
        #sonidos del juego
        self.sound_level = SoundUtil.loadSound(self, 'cosmic-air-way-arrange.ogg')
        self.sound_level.set_volume(self.volumen_musica)     
        self.sound_level.play()    
        
    def execute(self):
        
        ###############################codigo de prueba de creacion de enemigos##########################################
        #prueba, si no hay enemigos anado uno
        if len(self.enemies) <= 0:
            self.componentManager.createEnemies(self.enemies, self.velocidadJuego, self.vidas)     
        
        self.naveHeroe.pintar() 
        
        #eliminar enemigos
        enemigosParaBorrar = []
        for item in self.enemies:
            if(item.posicionY > self.screenWidth):
                item.borrar = True
            
            if item.borrar == True:
                enemigosParaBorrar.append(item)
                self.score += self.incremento_score
            else:
                item.pintar()
                item.ejecutarPatronMovimiento()
                
        self.enemies.remove(enemigosParaBorrar)
        self.naveHeroe.updateDisparos()
        ##################################################################################################################
    