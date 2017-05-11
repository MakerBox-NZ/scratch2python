#!/usr/bin/env python3
# draw a screen

# GNU All-Permissive License
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import pygame
import sys
import os

'''
Objects
'''

# put Python classes and functions here

'''
Setup
'''
screenX = 960
screenY = 720

fps = 40        # frame rate
afps = 4        # animation cycles
clock = pygame.time.Clock()
pygame.init()
main = True

screen = pygame.display.set_mode([screenX,screenY])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropRect = screen.get_rect()

'''
Main loop
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

#    screen.fill(black)
    screen.blit(backdrop, backdropRect)
    pygame.display.flip()
    clock.tick(fps)
