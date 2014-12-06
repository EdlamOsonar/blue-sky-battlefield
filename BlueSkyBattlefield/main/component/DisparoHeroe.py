from main.component.Disparo import Disparo
from main.component.NaveEnemiga import NaveEnemiga


class DisparoHeroe(Disparo):
    
    print('DisparoHeroe')
        
        
    def update(self):
        if self.borrar == False:
            self.posicionY = self.posicionY -10
            self.rect.y = self.posicionY
            self.rect.x = self.posicionX
                
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
        
        
    def colision(self, objetoColision):
        self.borrar = True
        if type(objetoColision) is NaveEnemiga:
            self.parentObject.score = self.parentObject.score + self.parentObject.incremento_score
        print 'disparo heroe collision. Puntuacion -> ' + str(self.parentObject.score)
    
