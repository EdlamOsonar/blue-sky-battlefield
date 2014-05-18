import pygame

from main.component.SpriteExtended import SpriteExtended
from main.util.ImageUtil import ImageUtils


class Disparo(SpriteExtended):
    
    def __init__(self, screen, image_dir, file_image_name, widthScale, heightScale):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = ImageUtils.load_image(screen, image_dir, file_image_name, True)
        self.scaledImage = pygame.transform.scale(self.image, (widthScale, heightScale))

        
    def pintar(self, initPosicionX, initPosicionY):                
        if self.borrar == False:
            self.posicionX = initPosicionX
            self.posicionY = initPosicionY
            self.rect.y = self.posicionY
            self.rect.x = self.posicionX
            
            self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
        
            
    def colision(self):
        self.borrar = True
        print 'disparo collision'