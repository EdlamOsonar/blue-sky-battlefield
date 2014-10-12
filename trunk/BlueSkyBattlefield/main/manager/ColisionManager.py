'''
Created on 03/05/2014

@author: Fernando
'''
import pygame

from main.component import DisparoEnemigo
from main.component.DisparoHeroe import DisparoHeroe
from main.component.NaveEnemiga import NaveEnemiga
from main.component.NaveHeroe import NaveHeroe



class ColisionManager(object):

    def __init__(self):
        self.disparosHeroe = pygame.sprite.Group()
        self.disparosEnemigo = pygame.sprite.Group()
        self.navesHeroe = pygame.sprite.Group()
        self.navesEnemigo = pygame.sprite.Group()
        
    # anade un objeto al array de colisiones para ser mantenido por el ColissionManager
    def add(self, item):
            if type(item) is DisparoHeroe:
                self.disparosHeroe.add(item)
            elif type(item) is DisparoEnemigo:
                self.disparosEnemigo.add(item)
            elif type(item) is NaveHeroe:
                self.navesHeroe.add(item)
            elif type(item) is NaveEnemiga:
                self.navesEnemigo.add(item)            
    
    # elimina un objeto al array de colisiones para ser mantenido por el ColissionManager    
    def remove(self, item):
        if type(item) is DisparoHeroe:
            self.disparosHeroe.remove(item)
        elif type(item) is DisparoEnemigo:
            self.disparosEnemigo.remove(item)
        elif type(item) is NaveHeroe:
            self.navesHeroe.remove(item)
        elif type(item) is NaveEnemiga:
            self.navesEnemigo.remove(item)
    
    # recorre el array de colisiones comprobando que los objetos colisionen, si colisionan lo notifica
    def execute(self):
        navesHeroe = self.navesHeroe.sprites()
        navesEnemigas = self.navesEnemigo.sprites()
        disparosHeroe = self.disparosHeroe.sprites()
        disparosEnemigo = self.disparosEnemigo.sprites()
        
        #colisiones nave heroe
        for indexNaveHeroe in xrange(len(navesHeroe)):
            if indexNaveHeroe < len(navesHeroe):
                naveHeroe = navesHeroe[indexNaveHeroe]
                #nave heroe con naves enemigas
                for indexNaveEnemiga in xrange(len(navesEnemigas)):
                    if indexNaveEnemiga < len(navesEnemigas):
                        naveEnemiga = navesEnemigas[indexNaveEnemiga]
                        if  pygame.sprite.collide_rect(naveHeroe, naveEnemiga):
                            naveHeroe.colision()
                            naveEnemiga.colision()
                            
        #colisiones disparos heroe
        for indexDisparoHeroe in xrange(len(disparosHeroe)):
            if indexDisparoHeroe < len(disparosHeroe):
                disparoHeroe = disparosHeroe[indexDisparoHeroe]
                for indexNaveEnemiga in xrange(len(navesEnemigas)):
                    if indexNaveEnemiga < len(navesEnemigas):
                        naveEnemiga = navesEnemigas[indexNaveEnemiga]
                        if pygame.sprite.collide_rect(disparoHeroe, naveEnemiga):
                            naveEnemiga.colision()
                            disparoHeroe.colision()
                            
        #colisiones disparos enemigos
        for indexDisparoEnemigo in xrange(len(disparosEnemigo)):
            if indexDisparoEnemigo < len(disparosEnemigo):
                disparoEnemigo = disparosEnemigo[indexDisparoEnemigo]
                for indexNaveHeroe in xrange(len(navesHeroe)):
                    if indexNaveHeroe < len(navesHeroe):
                        naveHeroe = navesHeroe[indexNaveHeroe]
                        if pygame.sprite.collide_rect(disparoEnemigo, navesHeroe):
                            naveHeroe.colision()
                            disparoEnemigo.colision()
                        