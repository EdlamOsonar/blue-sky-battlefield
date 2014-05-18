from main.component.Nave import Nave


class NaveEnemiga(Nave):
      
    
    def postConstructor(self):
        self.disparos = []
        self.vida = 10


    def atacar(self):
        print 'Nave enemiga ataca'
        
    def colision(self):
        self.vida = self.vida - 1
        if self.vida <= 0:
            self.explotar()

    def explotar(self):
        print 'pintar explosion'
        self.borrar = True
