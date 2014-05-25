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
            
