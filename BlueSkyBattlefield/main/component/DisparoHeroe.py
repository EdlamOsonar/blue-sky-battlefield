from main.component.Disparo import Disparo


class DisparoHeroe(Disparo):
    
    print('DisparoHeroe')
        
        
    def update(self):
        if self.borrar == False:
            self.posicionY = self.posicionY -10
            self.rect.y = self.posicionY
            self.rect.x = self.posicionX
                
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
        
        
    
