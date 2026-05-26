'''
Created on 11/10/2014

@author: Fernando
'''

import os
import pygame

class SoundUtil():

    SOUNDS_PATH = os.path.join('resources', 'sounds')

    @staticmethod
    def loadSound(caller, file_name):
        filename = os.path.join(SoundUtil.SOUNDS_PATH, file_name)
        sound = pygame.mixer.Sound(filename)

        return sound

    @staticmethod
    def getSound(caller, sound_index):
        return caller.soundList[sound_index]
