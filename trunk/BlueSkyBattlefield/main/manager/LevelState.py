import pygame
class LevelState():

    
    

    def resetAtributosGlobales(self, vidas):
        
        #group de enemigos    
        self.enemies = pygame.sprite.Group()
        
        #inicializacion de atributos de juego
        self.volumen_musica = 0.5
        self.level_number = 1
        self.vidas = vidas
        self.velocidadJuego = 1
        
        #creacion de la nave del heroe
        self.naveHeroe = self.componentManager.createNaveHeroe(self.screen, 'spaceShip_40.png', 'lasser.png', 25, 35, ((self.screenWidth / 2) - 20), (self.screenHeight - 65))
        self.naveHeroe.vidas = self.vidas 
        self.naveHeroe.velocidadMovimiento = self.velocidadJuego
        
    def getEnemies(self):
        return self.enemies

    def getVidas(self):
        return self.vidas

    def getLevelNumber(self):
        return self.level_number;
    
    def getVolumenMusica(self):
        return self.volumenMusica
        
    def getVelocidadJuego(self):
        return self.velocidadJuego
