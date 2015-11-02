import pygame
from main.component.Nave import Nave
from main.util.Constants import *


class NaveEnemiga(Nave):
      
    
    def postConstructor(self):
        self.disparos = []
        self.vida = 1

    def atacar(self):
        print 'Nave enemiga ataca'
            
    def ejecutarPatronMovimiento(self):
        
        if RUTINA_RECTO == self.rutina_movimiento:
            self.rutinaRecto()
        elif RUTINA_DIAGONAL == self.rutina_movimiento:
            self.rutinaDiagonal()
        elif RUTINA_DIAGONAL_DERECHA == self.rutina_movimiento:
            self.rutinaDiagonalDerecha()        
        else:
            self.posicionY = self.posicionY + (self.velocidad * 6)
            self.rect.y = self.posicionY
            if(self.posicionY > 200 and self.posicionY < 300):
                self.moverX(10)
    
    def rutinaRecto(self):
        self.posicionY = self.posicionY + (self.velocidad * 6)
        self.rect.y = self.posicionY
    
    def rutinaDiagonal(self):
        screenWidth = pygame.display.get_surface().get_width()
        if self.posicionX < screenWidth:
            self.posicionY = self.posicionY + (self.velocidad * 6)
            self.rect.y = self.posicionY
        else:
            self.posicionY = self.posicionY + (self.velocidad * 6)
            self.rect.y = self.posicionY
    
    def rutinaDiagonalDerecha(self):
        self.posicionY = self.posicionY + (self.velocidadJuego * 6)
        self.rect.y = self.posicionY
        self.posicionX = self.posicionX + 5
        self.rectX = self.posicionX       
            
    def toString(self):
        return  'NaveEnemiga'
            
