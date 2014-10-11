import pygame

from main.component.DisparoHeroe import DisparoHeroe
from main.component.Nave import Nave
from main.util.SoundUtil import SoundUtil
 

WIDTH_LASER = 3
HEIGHT_LASER = 5
NUMERO_DISPAROS = 25

class NaveHeroe(Nave):
    
    velocidadMovimiento = 15
    
    def postConstructor(self):       
        #crear aray de disparos
        self.disparos = pygame.sprite.Group()
        self.sonido_lasser = SoundUtil.loadSound(self, 'lasser_short.ogg')
        self.sonido_lasser.set_volume(0.5)
            
    def setColisionManager(self, colisionManager):
        self.colisionManager = colisionManager
    
    def moverIzquierda(self):
        self.moverX(-self.velocidadMovimiento)
    
    def moverDerecha(self):
        self.moverX(self.velocidadMovimiento)
        
    def moverArriba(self):
        self.moverY(-self.velocidadMovimiento)
        
    def moverAbajo(self):
        self.moverY(self.velocidadMovimiento)
        
    def disparar(self):
        if(len(self.disparos.sprites()) < NUMERO_DISPAROS):
            disparo = DisparoHeroe(self.screen, self.file_name_image_disparo, self.spriteSheet, WIDTH_LASER, HEIGHT_LASER)
            disparo.posicionX = self.posicionX + self.width / 2
            disparo.posicionY = self.posicionY
            self.disparos.add(disparo)                    
            self.colisionManager.add(disparo)            
            self.sonido_lasser.play()
            
    def updateDisparos(self):        
        if self.disparos.sprites():            
            numeroDisparos = len(self.disparos.sprites()) - 1
                       
            if(numeroDisparos >= 0):
                disparosEliminar  = []
                for disparo in self.disparos.sprites():
                    disparo.update() 
                    #comprobar si los disparos ya no estan en pantalla para eliminarlos
                    if disparo.posicionY < 0:
                        disparo.borrar = True            
                    
                    if disparo.borrar:
                        disparosEliminar.append(disparo)
                
                #eliminar disparos
                numeroDisparosEliminar = len(disparosEliminar) -1
                if numeroDisparosEliminar >= 0:
                    for i in range(numeroDisparosEliminar):
                        disparo = disparosEliminar[i]
                        self.disparos.remove(disparo)
                        self.colisionManager.remove(disparo)

    
    def colision(self):
        print 'colision de la nave del heroe'