from main.component.Nave import Nave
from main.component.DisparoHeroe import DisparoHeroe

WIDTH_LASER = 3
HEIGHT_LASER = 5
NUMERO_DISPAROS = 25

class NaveHeroe(Nave):
    
    velocidadMovimiento = 15
    
    def postConstructor(self):       
        #crear aray de arrayDisparos
        self.arrayDisparos = []
    
    def setColisionManager(self, colisionManager):
        self.colisionManager = colisionManager
    
    def moverIzquierda(self):
        self.moverX(-self.velocidadMovimiento)
    
    def moverDerecha(self):
        self.moverX(self.velocidadMovimiento)
        
    def disparar(self):
        if(len(self.arrayDisparos) < NUMERO_DISPAROS):
            disparo = DisparoHeroe(self.screen, self.image_dir, self.file_name_image_disparo, WIDTH_LASER, HEIGHT_LASER)
            disparo.posicionX = self.posicionX + self.width / 2
            disparo.posicionY = self.posicionY
            self.arrayDisparos.append(disparo)                    
            self.colisionManager.add(disparo)
            
    def updateDisparos(self):
        disparosEliminar = []                
        if self.arrayDisparos:            
            numeroDisparos = len(self.arrayDisparos)            
            
            for i in range(numeroDisparos):
                disparo = self.arrayDisparos[i]
                disparo.update() 
                #comprobar si los arrayDisparos ya no estan en pantalla para eliminarlos
                if disparo.posicionY <= 0:            
                    disparosEliminar.append(i)
                    #eliminar el disparo del colision manager
                    self.colisionManager.remove(disparo)
                    
            #eliminar los disparos que no se muestran
            for i in range(len(disparosEliminar)):                
                self.arrayDisparos.pop(disparosEliminar[i])     
    
    def colision(self):
        print 'colision de la nave del heroe'