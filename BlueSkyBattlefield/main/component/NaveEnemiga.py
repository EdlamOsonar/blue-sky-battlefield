from main.component.Nave import Nave
from pygame.sprite import Sprite


class NaveEnemiga(Nave):
      
    def postConstructor(self):
        self.arrayDisparos = []
        self.vida = 10
        
    def explotar(self, lasser):
       print('la nave del heroe ha hecho explotar la nave enmiga')
    
    def impacto(self):
        self.vida = self.vida - 1
        if self.vida <= 0:
            self.posicionY = self.posicionY - 50
            print 'El heroe PORNO ELOY mata al enemigo'
        
    def atacar(self):
        print 'ataca al heroe Porno Eloy'
        
    def collision(self):
        print 'nave enemiga collision'