'''
Created on 25/05/2014

@author: Fernando
'''
import pygame
import random
from ComponentManager import ComponentManager

class LevelManager():
    

    
    def __init__(self, screen, componentManager):
        'componente encargado de gestionar las fases del juego, los enemigos que se pintan, la vida del heroe, el numero de nivel, la puntucacion, etc'
        self.componentManager = componentManager
        self.screen = screen    
        
        #group de enemigos
        self.enemies = pygame.sprite.Group()
        
        self.level = 0
         
        #creacion de objetos nave del protagonista
        self.screenWidth = pygame.display.get_surface().get_width()
        self.screenHeight = pygame.display.get_surface().get_height()
        self.naveHeroe = self.componentManager.createNaveHeroe(self.screen, 'spaceShip_40.png', 'lasser.png', 25, 35, ((self.screenWidth / 2) - 20), (self.screenHeight - 65))
        
        
    
    def initLevel(self):
        self.vidas = 10           
        self.level += 1
        initSound = self.componentManager.soundManager.loadSound('dp_tron_panic.mp3')        
        initSound.play()

        
    def execute(self):
        self.naveHeroe.pintar() 
        
        #eliminar enemigos
        enemigosParaBorrar = []
        for item in self.enemies:
            if item.borrar == True:
                enemigosParaBorrar.append(item)
            else:
                item.pintar()
        self.enemies.remove(enemigosParaBorrar)
        
        #prueba, si no hay enemigos anado uno
        if len(self.enemies) <= 0:
            self.createEnemies()
                
    
    def createEnemies(self):
        posicionX = random.randint(1, self.screenWidth -21)        
        enemie = self.componentManager.createNaveEnemiga(self.screen,   'rd2.png', 'lasser.png', 25, 25, posicionX, (self.screenHeight - 400))
        #  enemie = self.componentManager.createNaveEnemiga(self.screen,   'rd2.png', 'lasser.png', 25, 25, ((self.screenWidth / 2) - 20), (self.screenHeight - 400))
        self.enemies.add(enemie)
        
        
          