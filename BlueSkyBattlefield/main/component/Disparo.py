import pygame

from main.util.ImageUtil import ImageUtils
from main.component.SpriteExtended import SpriteExtended

class Disparo(SpriteExtended):
    
    def __init__(self, screen, image_dir, file_image_name, widthScale, heightScale):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = ImageUtils.load_image(screen, image_dir, file_image_name, True)
        self.scaledImage = pygame.transform.scale(self.image, (widthScale, heightScale))

        
    def pintar(self, initPosicionX, initPosicionY):                
        self.posicionX = initPosicionX
        self.posicionY = initPosicionY
        self.rect.y = self.posicionY
        self.rect.x = self.posicionX
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
    
    def update(self):
        self.posicionY = self.posicionY -10
        self.rect.y = self.posicionY
        self.rect.x = self.posicionX
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
            
    def collision(self):
        print 'disparo collision'