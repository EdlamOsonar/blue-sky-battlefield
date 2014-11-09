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

VIDAS = 1
    
class LevelManager():  

   
    def __init__(self, screen, componentManager):
        'componente encargado de gestionar las fases del juego, los enemigos que se pintan, la vida del heroe, el numero de nivel, la puntucacion, etc'
        self.componentManager = componentManager
        self.screen = screen    
         
        #creacion de objetos nave del protagonista
        self.screenWidth = pygame.display.get_surface().get_width()
        self.screenHeight = pygame.display.get_surface().get_height()

        
        #inicializar el nivel 
        self.level = Level1(self.screen, self.componentManager, VIDAS)
        self.playGameOverSound = True
        self.initialScreen = True
        
    def getNaveHeroe(self):
        return self.level.naveHeroe
            
    def execute(self):
        #texto de las vidas
        self.font = pygame.font.Font('../resources/fonts/font.ttf', 8)
        vidasRender = self.font.render("Vidas x " +  str(self.level.vidas), 1, (255, 0, 0))
        self.screen.blit(vidasRender, (10, 12))   
        
        
        #texto del score
        self.font = pygame.font.Font('../resources/fonts/font.ttf', 8)
        scoreRender = self.font.render("Score%06d" % self.level.naveHeroe.score, 1, (255, 0, 0))
        self.screen.blit(scoreRender, (self.screenWidth - 100, 12))   
        
        #mover nave heroe
        self.moverNaveHeroe()
        
        #control de la vida del heroe
        if (self.level.naveHeroe.vida < 0):
            self.level.vidas = self.level.vidas -1
            self.level.naveHeroe.vida = VIDAS
                                  
                      
        #game over y reinicio
        if  self.initialScreen:
            self.initScreen()      
        elif self.level.vidas <= 0:
            self.gameOver()            
        elif self.level.vidas > 0:
            if(self.level.level_number == 1):
                self.level.execute()
        
    def moverNaveHeroe(self):
        #movimiento de la nave del heroe
        keys=pygame.key.get_pressed()   
        if (keys[pygame.K_a])or (keys[pygame.K_LEFT]):#move left
            self.getNaveHeroe().moverIzquierda()
        if(keys[pygame.K_d]) or (keys[pygame.K_RIGHT]):#move right
            self.getNaveHeroe().moverDerecha()
        if(keys[pygame.K_w]) or (keys[pygame.K_UP]):#move up
            self.getNaveHeroe().moverArriba()
        if(keys[pygame.K_s]) or (keys[pygame.K_DOWN]):#move down
            self.getNaveHeroe().moverAbajo()
        if(keys[pygame.K_SPACE]):
            self.getNaveHeroe().disparar()  
            
    def initScreen(self):
        #texto de la pantalla de inicio
        blueSkyBattlefieldRender = self.font.render("BLUE SKY BATTLEFIELD", 1, (255,0,0))
        self.screen.blit(blueSkyBattlefieldRender, ((self.screenWidth/2) - self.screenWidth / 9, (self.screenHeight/ 2)- self.screenHeight / 8))
        pressStartRender = self.font.render("PRESS START", 1, (255,0,0))
        self.screen.blit(pressStartRender, ((self.screenWidth/2) - self.screenWidth  / 18, (self.screenHeight/ 2)- 10))
        
        #resetear el juego al pulsar enter, mientras se queda esperando                        
        keys=pygame.key.get_pressed()   
        if (keys[pygame.K_RETURN]):            
            self.level.resetAtributosGlobales(VIDAS)
            self.level.resetLevelAtributes()
            self.initialScreen = False
            self.playGameOverSound = True   
    
    def gameOver(self):
        #game over
            #texto game over
            gameOverRender = self.font.render("GAME OVER", 1, (255,0,0))
            self.screen.blit(gameOverRender, ((self.screenWidth/2) - 20, (self.screenHeight/ 2)- 10))
                 
            if self.playGameOverSound:
                self.level.sound_level.stop()
                gameOverSound = SoundUtil.loadSound(self, 'game_over_robot.wav')
                gameOverSound.set_volume(self.level.volumen_musica)
                gameOverSound.play()
                self.playGameOverSound = False

            #resetear el juego al pulsar enter, mientras se queda esperando                        
            keys=pygame.key.get_pressed()   
            if (keys[pygame.K_ESCAPE]):
                self.initialScreen = True
                self.level.vidas = 0                
