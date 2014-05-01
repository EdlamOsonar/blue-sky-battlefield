from main.component.Disparo import Disparo
from main.component.Nave import Nave


class NaveHeroe(Nave):
    
    velocidadMovimiento = 15
    
    def postConstructor(self):
       
        #crear aray de arrayDisparos
        self.arrayDisparos = [Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5),
                             Disparo(self.screen, self.image_dir, self.file_name_image_disparo, 3, 5)]
        
        self.disparosDisponibles = len(self.arrayDisparos) -1
    
    def moverIzquierda(self):
        self.moverX(-self.velocidadMovimiento)
    
    def moverDerecha(self):
        self.moverX(self.velocidadMovimiento)
        
    def disparar(self):
         
        if self.disparosDisponibles >= 0:            
            if self.arrayDisparos[self.disparosDisponibles].enabled == False:                        
                self.arrayDisparos[self.disparosDisponibles].pintar(self.posicionX , self.posicionY)     
                self.arrayDisparos[self.disparosDisponibles].enabled = True           
        else:
            self.disparosDisponibles = len(self.arrayDisparos) -1
          
        self.disparosDisponibles = self.disparosDisponibles - 1        
            
    def updateDisparos(self):
        for i in xrange(len(self.arrayDisparos) -1):
            self.arrayDisparos[i].update() 
                        
            #comprobar si los arrayDisparos ya no estan en pantalla para disminuir el contao de arrayDisparos (solo puede haber self.disparosDisponibles en pantalla)
            if self.arrayDisparos[i].posicionY < 0 and self.arrayDisparos[i].enabled == True:                
                self.arrayDisparos[i].posicionX = self.posicionX
                self.arrayDisparos[i].posicionY = self.posicionY
                self.disparosDisponibles = self.disparosDisponibles + 1
                self.arrayDisparos[i].enabled = False
            print("disparo -> " + str(i) + " posicion en pantalla en el eje y " + str(self.arrayDisparos[i].posicionY) + " enabled = " + str(self.arrayDisparos[i].enabled))
