'''
Created on 25/05/2014

@author: Fernando
'''
import pygame
import random
from main.util.SoundUtil import SoundUtil

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
        
        #inicializacion de atributos de juego
        self.volumen_musica = 0.5
        self.vidas = 10
        self.score = 0
        self.incremento_score = 125
        self.velocidadJuego = 1
        
    def initLevel(self):                   
        self.level += 1
        sound_level = SoundUtil.loadSound(self, 'cosmic-air-way-arrange.ogg')
        sound_level.set_volume(self.volumen_musica)     
        sound_level.play()
        
    def execute(self):
        #prueba, si no hay enemigos anado uno
        if len(self.enemies) <= 0:
            self.createEnemies()     
        
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
        

            
        self.font = pygame.font.Font('../resources/fonts/font.ttf', 8)
        scoreRender = self.font.render("Score%06d" % self.score, 1, (255, 0, 0))        
        self.screen.blit(scoreRender, (self.screenWidth - 100, 12))           
        self.naveHeroe.updateDisparos()
        
    def createEnemies(self):
        posicionX = random.randint(1, self.screenWidth -21)        
        enemie = self.componentManager.createNaveEnemiga(self.screen,   'rd2.png', 'lasser.png', 25, 25, posicionX, (self.screenHeight - 400))
        #  enemie = self.componentManager.createNaveEnemiga(self.screen,   'rd2.png', 'lasser.png', 25, 25, ((self.screenWidth / 2) - 20), (self.screenHeight - 400))
        enemie.velocidad = self.velocidadJuego
        self.enemies.add(enemie)