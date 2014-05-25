'''
Created on 25/05/2014

@author: Fernando
'''
import pygame
import os
class SoundManager():
    

    def __init__(self):        
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)  
    
    def loadSound(self, filename):
        filename = os.path.join('../resources/sounds', filename)
        return pygame.mixer.Sound(filename)