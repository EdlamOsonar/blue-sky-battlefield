from main.component.Nave import Nave
from main.util.Constants import RUTINA_RECTO


class NaveEnemiga(Nave):
      
    
    def postConstructor(self):
        self.disparos = []
        self.vida = 2

    def atacar(self):
        print 'Nave enemiga ataca'
        
    def colision(self):
        self.vidas = self.vidas - 1
        if self.vidas <= 0:
            self.explotar()

    def explotar(self):
        print 'pintar explosion'
        self.borrar = True
        for item in self.explosion:
            self.screen.blit(item, (self.posicionX, self.posicionY))
            
    def ejecutarPatronMovimiento(self):
        
        if RUTINA_RECTO == self.rutina_movimiento:
            self.posicionY = self.posicionY + (self.velocidad * 6)
            self.rect.y = self.posicionY
        else:
            self.posicionY = self.posicionY + (self.velocidad * 6)
            self.rect.y = self.posicionY
            if(self.posicionY > 200 and self.posicionY < 300):
                self.moverX(10)
            
            
    def toString(self):
        return  'NaveEnemiga'
            
