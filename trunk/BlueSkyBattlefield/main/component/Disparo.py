import pygame

from main.component.SpriteExtended import SpriteExtended
from main.util.ImageUtil import SpriteSheet
from main.util.ImageUtil import SPRITE_SHEET

class Disparo(SpriteExtended):
    
    def __init__(self, screen, file_image_name, spriteSheet, widthScale, heightScale):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = SpriteSheet(SPRITE_SHEET)
        self.image = spriteSheet.imgat((48, 176, 9, 20), -1)
        self.rect = self.image.get_rect()
        #self.image, self.rect = ImageUtils.load_image(file_image_name)
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