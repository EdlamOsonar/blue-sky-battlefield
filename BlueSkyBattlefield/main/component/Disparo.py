import pygame

from main.util.ImageUtil import ImageUtils


class Disparo(pygame.sprite.Sprite):
    
    def __init__(self, screen, image_dir, file_image_name, widthScale, heightScale):
        self.screen = screen
        self.image = ImageUtils.load_image(screen, image_dir, file_image_name, True)
        self.scaledImage = pygame.transform.scale(self.image, (widthScale, heightScale))
        self.posicionX = 0
        self.posicionY = 0
        
    def pintar(self, initPosicionX, initPosicionY):        
        self.posicionX = initPosicionX
        self.posicionY = initPosicionY
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
    
    def update(self):
        self.posicionY = self.posicionY -10
        self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
            