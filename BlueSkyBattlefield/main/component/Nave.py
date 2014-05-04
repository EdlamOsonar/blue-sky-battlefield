import pygame

from main.util.ImageUtil import ImageUtils
from main.component.SpriteExtended import SpriteExtended

class Nave(SpriteExtended):    
       
    #screen y filename son la pantalla y la ruta del archivo que le pasamos al metodo loadImage
    #widthScale, heightScale son el reescalado del sprite , posicionX, posicionY son el lugar de la pantalla
    #en que queremos que se pinte el sprite
    def __init__(self, screen, image_dir, imagen, imagen_disparo, widthScale, heightScale, posicionX, posicionY):        
        self.screen = screen
        self.image_dir = image_dir
        
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = ImageUtils.load_image(screen, image_dir, imagen, True)
        self.file_name_image_disparo = imagen_disparo
        
        self.scaledImage = pygame.transform.scale(self.image, (widthScale, heightScale))
        
        #posiciones en pantalla y tamano del objeto
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.rect.y = self.posicionY
        self.rect.x = self.posicionX
        self.width = widthScale
        self.height = heightScale
        
        self.postConstructor()

    def postConstrucor(self):
        pass
    
    def collision(self):
        pass
    
    def pintar(self):
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
        
    def moverX(self, unidades):       
        nuevaPosicion = self.posicionX + unidades
        if nuevaPosicion > -2 and nuevaPosicion < self.screen.get_width() - 21:
            self.posicionX = self.posicionX + unidades
            self.rect.x = self.posicionX

    def moverY(self, unidades):
        self.posicionY = self.posicionY + unidades
        
    
    