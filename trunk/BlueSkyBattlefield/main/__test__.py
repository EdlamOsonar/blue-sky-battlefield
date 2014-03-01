#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
import random
from pygame.locals import*
import sys
import os
from locale import str


# Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMAGE_DIR = "imx"

lstRects = []

# Clases
# ---------------------------------------------------------------------
class Nave():
    def __init__(self, image, posX, posY):
            
            #sprite de la nave
            self.sprite = pygame.sprite.Sprite()
            self.sprite.image = image
            self.sprite.rect = image.get_rect()
            self.sprite.rect.top = posY
            self.sprite.rect.left = posX
            
            #lista de disparos y su estado, disparando indica si se ha pulsado el boton de disparar 
            self.disparos = []
            self.disparando = False
            for item in range(5):
                self.disparos.append(pygame.Rect(0, 0, 2, 30))   
   
    def mover(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                self.sprite.rect.move_ip(-10, 0)
            if evento.key == pygame.K_RIGHT:
                self.sprite.rect.move_ip(10, 0)
    
    def disparar(self, screen, color):
        self.disparando = True    
        for rect in self.disparos:
            rect.move(self.sprite.rect.left + (self.sprite.rect.width / 2),
                      self.sprite.rect.top - (self.sprite.rect.height / 2))

    def moverDisparos(self, screen, color):
        if self.disparando == True:
            for disparo in self.disparos:
                pygame.draw.rect(screen, color, disparo)
                disparo.move_ip(0, -10)
        
        
# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def load_image(screen, filename, transparent=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(IMAGE_DIR, filename)
    print ruta
    try:
        image = pygame.image.load(ruta)
    except pygame.error, message:
        raise  SystemExit(message)

    if transparent:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


def crearRectangulosEnemigosVariables(numeroRectangulos):    
    for i in range(numeroRectangulos):
        w = random.randrange(10, 30)
        h = random.randrange(10, 40)
        x = random.randrange(30, 600)
        y = random.randrange(10, 100) 
        lstRects.append(pygame.Rect(x, y, w, h))
        
        print "anadido a la lista de rectangulos el rectangulo numero " + str(i)

        
def pintarRectangulosEnemigos(screen, color):
    for rect in lstRects:
        pygame.draw.rect(screen, color, rect)
        
        
def moverRectangulosEnemigos(lstRects, execute):
    if execute == True:
        for rect in lstRects:            
            rect.move_ip(0, 1)
            print "posicion del rectangulo " + str(rect.top)
          
            
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Blue Space Battlefield")

    #load images
    background_image = load_image(screen, 'stars_blue.png')
    spaceship_image = load_image(screen, 'spaceShip_40.png', True)
        
    #colores planos
    colorRojo = pygame.Color(184,0, 46)
    colorAzul = pygame.Color(0,46, 184)
    
    #rectangulos
    rect1 = pygame.Rect(50,50, 20,30)
    rect2 = pygame.Rect(320, 240, 30, 20)   
    #crear rectangulos aleatorios
    crearRectangulosEnemigosVariables(25)
    
    #sprite de la nave principal
    nave = Nave(spaceship_image, 310, 420)
            
    #Bucle principal del juego
    salir = False    
    reloj = pygame.time.Clock();
    
    #detener el scroll de los enemigos
    mover = False
    
    while salir != True:
        #set images position
        screen.blit(background_image, (0, 0))
        #screen.blit(spaceship_image, ((SCREEN_WIDTH / 2) - 20, SCREEN_HEIGHT - 65))
        screen.blit(nave.sprite.image, nave.sprite.rect)

        #posicion x e y del rectangulo 1 antes del movimiento
        (xPrevious, yPrevious) = (rect1.left, rect1.top)
        
        #asignar la posicion del rectangulo a la posicion del raton
        (rect1.left, rect1.top) = pygame.mouse.get_pos()       
        #ajustar la posicion del rectangulo a la posicion del cursor con los anchos del rectangulo
        rect1.left -= rect1.width / 2
        rect1.top -= rect1.height / 2
        
        #control de colisiones, si colisionan devolvemos el rectangulo uno a la posicion anterior al movimiento
        if rect1.colliderect(rect2):
            (rect1.left, rect1.top) = (xPrevious, yPrevious)
                
        for evento in pygame.event.get():
            #movimiento de la nave
            nave.mover(evento)
            
            #pruebas de crear rectangulos variables y seguir el cursor con un rectangulo
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    mover  = True
                if evento.key == pygame.K_ESCAPE:
                    mover = False  
                    crearRectangulosEnemigosVariables(25)
                if evento.key == pygame.K_SPACE:
                    nave.disparar(screen, colorAzul)
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.set_pos(320, 240)
                
            if evento.type == QUIT:
                salir = True
        
        #mover los disparos de la nave
        nave.moverDisparos(screen, colorAzul)
        
        #reloj que controla la velocidad de ejecucion del juego
        reloj.tick(25)

        #pintar rectangulo        
        pygame.draw.rect(screen, colorRojo, rect1)
        pygame.draw.rect(screen, colorAzul, rect2)            

        #pintar lista de rectangulos de tamano aleatorio
        pintarRectangulosEnemigos(screen, colorRojo)
        #pygame.draw.rect(screen, colorRojo, rect1, 100)  
        
        moverRectangulosEnemigos(lstRects, mover)
        
        pygame.display.flip()
        
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()



