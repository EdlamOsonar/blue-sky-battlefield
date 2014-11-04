'''
Created on 25/05/2014

@author: Fernando
'''
import pygame
import random
from main.util.Constants import RUTINA_RECTO
from main.util.SoundUtil import SoundUtil
from main.manager.ComponentManager import ComponentManager
from main.level.Level1 import Level1

VIDAS = 10
    
class LevelManager():  

   
    def __init__(self, screen, componentManager):
        'componente encargado de gestionar las fases del juego, los enemigos que se pintan, la vida del heroe, el numero de nivel, la puntucacion, etc'
        self.componentManager = componentManager
        self.screen = screen    
         
        #creacion de objetos nave del protagonista
        self.screenWidth = pygame.display.get_surface().get_width()
        self.screenHeight = pygame.display.get_surface().get_height()

        
        #inicializar el nivel 
        self.level = Level1(self.screen, self.componentManager)
        self.playGameOverSound = True
        
    def getNaveHeroe(self):
        return self.level.naveHeroe
            
    def execute(self):
        #texto del score
        self.font = pygame.font.Font('../resources/fonts/font.ttf', 8)
        scoreRender = self.font.render("Score%06d" % self.level.getScore(), 1, (255, 0, 0))
        self.screen.blit(scoreRender, (self.screenWidth - 100, 12))   
                
                
        if (self.level.naveHeroe.vida < 0):
            self.level.vidas = self.level.vidas -1
                      
        if self.level.vidas > 0:
            if(self.level.level_number == 1):
                self.level.execute()
                self.playGameOverSound = True        
        else:            
            #game over
            #texto game over
            gameOverRender = self.font.render("GAME OVER", 1, (255,0,0))
            self.screen.blit(gameOverRender, ((self.screenWidth/2) - 20, (self.screenHeight/ 2)- 10))
            self.level.sound_level.stop()
                 
            if self.playGameOverSound:
                gameOverSound = SoundUtil.loadSound(self, 'game_over_robot.wav')
                gameOverSound.set_volume(self.level.volumen_musica)
                gameOverSound.play()
                self.playGameOverSound = False
            
        
        
            #resetear el juego al pulsar enter, mientras se queda esperando                        
            print 'pulsa enter para reiniciar'
            keys=pygame.key.get_pressed()   
            if (keys[pygame.K_RETURN]):
                self.level.resetAtributosGlobales()
                self.level.resetLevelAtributes()


    def createEnemies(self, screen, componentManager):
        posicionX = random.randint(1, self.screenWidth -21)        
        enemie = componentManager.createNaveEnemiga(screen,   'rd2.png', 'lasser.png', 25, 25, posicionX, (pygame.display.get_surface().get_height() - 400), RUTINA_RECTO)
        #  enemie = self.componentManager.createNaveEnemiga(self.screen,   'rd2.png', 'lasser.png', 25, 25, ((self.screenWidth / 2) - 20), (self.screenHeight - 400), RUTINA_RECTO)
        enemie.velocidad = self.level.getVelocidadJuego()
        self.level.getEnemies().add(enemie)
        
    #Crea una rutina de dos enemigos que avanzan en paralelo hacia abajo
    #desde cada extremo de la pantalla    
    def rutinaEnemigosEnParalelo(self, imagen, imagen_disparo, widthScale, heightScale):
        ComponentManager.createNaveEnemiga(self, self.screen, imagen, imagen_disparo, widthScale, heightScale, 10, RUTINA_RECTO)       
        ComponentManager.createNaveEnemiga(self, self.screen, imagen, imagen_disparo, widthScale, heightScale, self.screen.width - 10, RUTINA_RECTO)