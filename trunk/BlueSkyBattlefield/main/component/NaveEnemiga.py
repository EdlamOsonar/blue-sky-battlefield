from main.component.Nave import Nave


class NaveEnemiga(Nave):
      
    
    def postConstructor(self):
        self.disparos = []
        self.vida = 2

    def atacar(self):
        print 'Nave enemiga ataca'
        
    def colision(self):
        self.vida = self.vida - 1
        if self.vida <= 0:
            self.explotar()

    def explotar(self):
        print 'pintar explosion'
        self.borrar = True
        for item in self.explosion:
            self.screen.blit(item, (self.posicionX, self.posicionY))
            
    def ejecutarPatronMovimiento(self):
        self.posicionY = self.posicionY + (self.velocidad * 6)
        self.rect.y = self.posicionY
        if(self.posicionY > 200 and self.posicionY < 300):
            self.moverX(10)
            
            
    def toString(self):
        return  'NaveEnemiga'
            
