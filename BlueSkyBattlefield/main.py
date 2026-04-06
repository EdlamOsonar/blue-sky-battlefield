#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Blue Sky Battlefield - Async entry point for pygbag/web and direct execution.
"""

import asyncio
import sys
import os

# Set working directory to the game root (folder containing this file)
# so all relative resource paths resolve correctly in both native and web builds.
_here = os.path.dirname(os.path.abspath(__file__))
os.chdir(_here)
if _here not in sys.path:
    sys.path.insert(0, _here)

import pygame
from pygame.locals import QUIT

from main.manager.ColisionManager import ColisionManager
from main.manager.ComponentManager import ComponentManager
from main.manager.LevelManager import LevelManager

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


async def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Blue Sky Battlefield")
    pygame.mouse.set_visible(False)

    componentManager = ComponentManager(screen)
    levelManager = LevelManager(screen, componentManager)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        if levelManager.inExecute:
            componentManager.landScapeManager.scrollLandScape()
        componentManager.landScapeManager.update(levelManager.inExecute)

        levelManager.execute()
        componentManager.colisionManager.execute()
        componentManager.checkRemove()

        clock.tick(30)
        pygame.display.update()
        pygame.display.flip()

        # Required by pygbag to yield control back to the browser event loop
        await asyncio.sleep(0)

    pygame.quit()


if __name__ == '__main__':
    asyncio.run(main())
