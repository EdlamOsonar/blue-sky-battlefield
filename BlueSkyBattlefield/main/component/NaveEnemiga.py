from main.component.Nave import Nave



class NaveEnemiga(Nave):
      
    def postConstructor(self):
        self.arrayDisparos = []
        self.vida = 10


    def atacar(self):
        print 'Nave enemiga ataca'
        
    def colision(self):
        self.vida = self.vida - 1
        if self.vida <= 0:
            self.posicionY = self.posicionY - 50
            self.posicionY = self.posicionY -50
            print 'Nave Enemiga destruida'
            
            
        print 'vida de la nave enemiga ' + str(self.vida)