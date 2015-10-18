import pygame
from main.component.SpriteExtended import SpriteExtended


class ScoreBar(SpriteExtended):
    
    
     
    def __init__(self, screen, puntosVida, scoreBarSize = None):
        self.screen = screen
        
        if scoreBarSize:            
            self.scoreBarSize = scoreBarSize
        else:
            self.scoreBarSize = 6
        self.posicionX = 20
        self.posicionY = 140
        
        scoreWidht = 16
        scoreHeight = 16
        
        colorRojo = pygame.Color(255,0, 0)
        colorNaranja  = pygame.Color(253, 92, 23)
        colorAmarillo = pygame.Color(255,205, 0)
        colorVerdeClaro = pygame.Color(157, 217, 44)
        colorVerde = pygame.Color(27, 202, 33)
        colorAzul = pygame.Color(27, 202, 155)
        
        colores = [colorRojo, colorRojo, colorNaranja, colorAmarillo, colorAmarillo,
                    colorVerdeClaro, colorVerde]
        
        for item in range(puntosVida):
            posicionVertical = self.posicionY - (scoreHeight * (item +1))
            color = colores[item]
            self.rect = pygame.draw.rect(screen, color,(self.posicionX, posicionVertical,
                                                         scoreWidht, scoreHeight))
        