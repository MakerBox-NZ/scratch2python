#!/usr/bin/env python3
# draw a screen
# add a player and player control
# add player movement
# add platforms
# add gravity
# add collisions
# add jump
# add scrolling

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
class Platform(pygame.sprite.Sprite):
    '''
    Create a platform
    '''
    # x location, y location, image width, image height, image file    
    def __init__(self,xloc,yloc,imgw,imgh,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([imgw,imgh])
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.blockpic = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc
        
        # paint the image into the blocks
        self.image.blit(self.blockpic,(0,0),(0,0,imgw,imgh))

class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.momentumX = 0
        self.momentumY = 0
        self.frame     = 0
        # gravity variables
        self.collide_delta = 0
        self.jump_delta    = 6
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

    def update(self,platform_list):
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

        # collisions
        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        if self.momentumX > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                self.rect.x = currentX+9
                # gravity
                self.momentumY     = 0
                self.collide_delta = 0

        if self.momentumY > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                # gravity
                self.momentumY     = 0
                self.collide_delta = 0

        # gravity
        if self.collide_delta < 6 and self.jump_delta < 6:
            self.jump_delta     = 6*2
            self.momentumY     -= 33  # how high to jump

            self.collide_delta += 6
            self.jump_delta    += 6

    def jump(self,platform_list):
        self.jump_delta = 0

    def gravity(self):
        self.momentumY += 3.2  # how fast player falls

        if self.rect.y > screenY and self.momentumY >= 0:
            self.momentumY     = 0
            self.rect.y        = screenY
            
# map where the platforms go
# x location, y location, image width, image height, image file
def level1():
    platform_list = pygame.sprite.Group()
    block = Platform(0,591,1920,129, os.path.join('images','block0.png'))
    platform_list.add(block)
    block = Platform(20,427,173,72, os.path.join('images','block1.png'))
    platform_list.add(block)
    block = Platform(60,227,337,72, os.path.join('images','block2.png'))
    platform_list.add(block)
    return platform_list

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
platform_list = level1()
player = Player()   # spawn player
player.rect.x = 10
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10      # how fast to move
forwardX  = 600     # when to scroll
backwardX = 230     # when to scroll

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
                player.jump(platform_list)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(movesteps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-movesteps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    # scroll the world forward
    if player.rect.x >= forwardX:
        scroll = player.rect.x - forwardX
        player.rect.x = forwardX
        for platform in platform_list:
            platform.rect.x -= scroll

    # scroll the world backward
    if player.rect.x <= backwardX:
        scroll = min(1,(backwardX - player.rect.x))
        player.rect.x = backwardX
        for platform in platform_list:
            platform.rect.x += scroll
                
#    screen.fill(black)
    screen.blit(backdrop, backdropRect)
    platform_list.draw(screen)   # refresh platforms
    player.gravity()             # check gravity
    player.update(platform_list) # refresh player
    movingsprites.draw(screen)   # refresh player position
    pygame.display.flip()
    clock.tick(fps)
