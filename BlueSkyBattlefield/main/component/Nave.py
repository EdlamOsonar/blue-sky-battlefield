import pygame

from main.component.SpriteExtended import SpriteExtended
from main.util.ImageUtil import ImageUtils
from main.util.ImageUtil import SpriteSheet
from main.util.ImageUtil import SPRITE_SPACESSHIP
from main.util.ImageUtil import SPRITE_SHEET
from main.util.Constants import *

class Nave(SpriteExtended):    
    
    
       
    #screen y filename son la pantalla y la ruta del archivo que le pasamos al metodo loadImage
    #widthScale, heightScale son el reescalado del sprite , posicionX, posicionY son el lugar de la pantalla
    #en que queremos que se pinte el sprite
    def __init__(self, screen, image_rects, imagen_disparo, widthScale, heightScale, posicionX, posicionY):        
        self.screen = screen
                
        pygame.sprite.Sprite.__init__(self)       
                
        #space_ship = sprite_sheet_space_ship.imgsat([(100,100, 32,32)], -1)
        sprite_sheet_space_ship = SpriteSheet(SPRITE_SPACESSHIP)
        space_ship = sprite_sheet_space_ship.imgsat(image_rects, -1)
        self.rect = space_ship[0].get_rect()       
        #self.image, self.rect = ImageUtils.load_image(imagen, None, True )
        
        self.spriteSheet = SpriteSheet(SPRITE_SHEET)
        self.explosion = self.spriteSheet.imgsat([(70, 169, 32, 32),
                                           (103, 169, 32, 32),
                                           (136, 169, 32, 32),
                                           (169, 169, 32, 32),
                                           (202, 169, 32, 32),                                           
                                           (235, 169, 32, 32)],
                                          -1)
        
        self.file_name_image_disparo = imagen_disparo
        
        #self.scaledImage = pygame.transform.scale(self.image, (widthScale, heightScale))
        self.scaled_image = []
        for index in xrange(len(space_ship)):
            self.scaled_image.append(pygame.transform.scale(space_ship[index], (widthScale, heightScale)))
    
        #posiciones en pantalla y tamano del objeto
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.rect.y = self.posicionY
        self.rect.x = self.posicionX
        self.width = widthScale

        #array que describe el tipo de movimiento, lateral y vertical
        self.move_type = [MOVE_RECT, MOVE_NONE]
        self.postConstructor()

    def postConstrucor(self):
        pass

    def colision(self, objetoColision):
        self.vidas = self.vidas - 1
        if self.vidas <= 0:
            self.explotar()

    def explotar(self):
        print 'pintar explosion'
        self.borrar = True
        for item in self.explosion:
            self.screen.blit(item, (self.posicionX, self.posicionY))    

    
    def pintar(self):
        if self.borrar == False:
            #self.screen.blit(self.scaledImage, (self.posicionX, self.posicionY))
            
            #calcular el indice de la animacion de la nave en funcion del movimiento
            move_image_index = MOVE_RECT
            
            if self.move_type[0] == MOVE_LEFT and self.move_type[1] == MOVE_NONE:
                move_image_index = MOVE_LEFT
            elif self.move_type[0] == MOVE_RIGHT and self.move_type[1] == MOVE_NONE:
                move_image_index = MOVE_LEFT
            elif self.move_type[0] == MOVE_RECT and self.move_type[1] == MOVE_UP:
                move_image_index = MOVE_UP
            elif self.move_type[0] == MOVE_RECT and self.move_type[1] == MOVE_DOWN:
                move_image_index = MOVE_RECT
            elif self.move_type[0] == MOVE_LEFT and self.move_type[1] == MOVE_UP:
                move_image_index = MOVE_UP_LEFT
            elif self.move_type[0] == MOVE_RIGHT and self.move_type[1] == MOVE_UP:
                move_image_index = MOVE_UP_RIGHT
            elif self.move_type[0] == MOVE_LEFT and self.move_type[1] == MOVE_DOWN:
                move_image_index = MOVE_LEFT    
            elif self.move_type[0] == MOVE_RIGHT and self.move_type[1] == MOVE_DOWN:
                move_image_index = MOVE_RIGHT
                            
            self.screen.blit(self.scaled_image[move_image_index], (self.posicionX, self.posicionY))
            
    def moverX(self, unidades):       
        nuevaPosicion = self.posicionX + unidades
        
        if nuevaPosicion > self.posicionX:
            self.move_type[0] = MOVE_RIGHT
        else:
            self.move_type[0] = MOVE_LEFT
            
        if nuevaPosicion > -2 and nuevaPosicion < self.screen.get_width() - 21:
            self.posicionX = self.posicionX + unidades
            self.rect.x = self.posicionX

    def moverY(self, unidades):
        nuevaPosicion = self.posicionY + unidades
        
        if nuevaPosicion < self.posicionY:
            self.move_type[1] = MOVE_UP
        else:
            self.move_type[1] = MOVE_DOWN
            
        if nuevaPosicion > -2 and nuevaPosicion < self.screen.get_height() - 21:
            self.posicionY = self.posicionY + unidades
            self.rect.y = self.posicionY
    
    def no_mover(self):
        self.move_type[0] = MOVE_RECT
        self.move_type[1] = MOVE_NONE
    
    