#!/usr/bin/env python3
# draw a screen
# add a player and player control
# add player movement

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

class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.momentumX = 0
        self.momentumY = 0
        self.frame = 0
        self.images = []
        for i in range(1,9):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(alpha)
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

    def control(self,x,y):
        '''
        control player movement
        '''
        self.momentumX += x
        self.momentumY += y

    def update(self):
        '''
        Update sprite position
        '''

        currentX = self.rect.x
        nextX = currentX+self.momentumX
        self.rect.x = nextX

        currentY = self.rect.y
        nextY = currentY+self.momentumY
        self.rect.y = nextY

        # moving left
        if self.momentumX < 0:
            self.frame += 1
            if self.frame > 3*afps:
                self.frame = 0
            self.image = self.images[self.frame//afps]

        # moving right
        if self.momentumX > 0:
            self.frame += 1
            if self.frame > 3*afps:
                self.frame = 0
            self.image = self.images[self.frame//afps+4]


'''
Setup
'''
alpha = (0,0,0)
black = (0,0,0)
white = (255,255,255)
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
player = Player()   # spawn player
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10      # how fast to move

'''
Main loop
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-movesteps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(movesteps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(movesteps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-movesteps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

#    screen.fill(black)
    screen.blit(backdrop, backdropRect)
    player.update()
    movingsprites.draw(screen) #refresh player position
    pygame.display.flip()
    clock.tick(fps)
