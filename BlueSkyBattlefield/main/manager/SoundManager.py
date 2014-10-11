'''
Created on 25/05/2014

@author: Fernando
'''
import pygame
import os

class SoundManager():
    def __init__(self):        
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
        self.soundList = []
    
    def loadSound(self, sound_index, file_name):
        filename = os.path.join('../resources/sounds', file_name)
        sound = pygame.mixer.Sound(filename)                
        self.soundList.insert(sound_index, sound)                
        return sound
    
    def getSound(self, sound_index):       
        return self.soundList[sound_index]