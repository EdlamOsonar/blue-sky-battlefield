'''
Created on 11/10/2014

@author: Fernando
'''

import os
import pygame

class SoundUtil():
    
    @staticmethod
    def loadSound(self, file_name):
        filename = os.path.join('../resources/sounds', file_name)
        sound = pygame.mixer.Sound(filename)               
                
        return sound
    @staticmethod
    def getSound(self, sound_index):       
        return self.soundList[sound_index]
