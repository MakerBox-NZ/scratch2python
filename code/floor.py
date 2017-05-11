#!/usr/bin/env python3
# platforms + animation

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

        self.createBlock(0,0,xloc,yloc,imgw,imgh,img)
        self.image.convert_alpha()
        self.image.set_colorkey(black)

    def createBlock(self,offsetx,offsety,xloc,yloc,imgw,imgh,img):
        blockpic = pygame.image.load(img).convert()
        self.image = pygame.Surface([imgw,imgh])
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc
        
        # paint the ledge
        self.image.blit(blockpic,(offsetx,offsety),(offsetx,offsety,imgw,imgh))
        
class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    momentumX = 0
    momentumY = 0
    frame = 0

    # gravity variables
    jumping = False
    frame_since_collision = 0
    frame_since_jump = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #animation
        self.images = []
        for i in range(1,9):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(black)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self,x,y):
        '''
        control player movement
        '''
        self.momentumX += x
        self.momentumY += y

    def update(self, blocker):
        '''
        Find collisions
        '''

        # collision horizontal
        currentX = self.rect.x
        nextX = currentX+self.momentumX
        self.rect.x = nextX

        # collision vertical
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

        # detect collisions with ledges via 'blocker' argument
            # this has minor improvement over the code in the book
            # by adding movement along the X axis
        block_hit_list = pygame.sprite.spritecollide(self, blocker, False)
        if self.momentumX > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                self.rect.x = currentX+9
            # gravity
                self.momentumY = 0
                self.frame_since_collision = 0

        if self.momentumY > 0:
            for block in block_hit_list:
                self.rect.y = currentY
            # gravity
                self.momentumY = 0
                self.frame_since_collision = 0

        # gravity
        if self.frame_since_collision < 6 and self.frame_since_jump < 6:
            self.frame_since_jump = 0
            self.momentumY -= 12
            # increment frames since collision and jump
            # set to 6 for no in-air jumps
            # set to less for possible in-air and wall- jumps
            self.frame_since_collision += 6
            self.frame_since_jump += 6

    # anti gravity
    def jump(self,blocker):
        self.jumping = True
        self.frame_since_jump = 0

    def gravity(self):
        # greater number here = heavier gravity
        self.momentumY += .47
        # use screenU as "the ground"
        if self.rect.y > screenU and self.momentumY >= 0:
            self.momentumY = 0
            # if we hit the ground (screenU) then we die
            pygame.QUIT; sys.exit()
            main = False
            # or you could use this code to
            # just solidify the ground, no death included
#            self.rect.y = screenU
#            self.frame_since_collision = 0

# set where all the platforms go
# x location, y location, image width, image height, image file
def createWorld():
    ledge_list = pygame.sprite.Group()
    ledge = Platform(0,327,1920,393, 'plat0.png')
    ledge_list.add(ledge)
    ledge = Platform(0,0,412,392, 'plat1.png')
    ledge_list.add(ledge)
    ledge = Platform(600,100,421,217, 'plat2.png')
    ledge_list.add(ledge)
    ledge = Platform(1552,389,368,331,'plat3.png')
    ledge_list.add(ledge)
    return ledge_list

'''
Setup
'''
alpha = (255,255,255)
black = (0,0,0)
white = (255,255,255)
screenX = 960
screenY = 720
screenU = 680

forwardX = 590  # when to scroll
backwardX = 230 # when to scroll
movesteps = 10  # how fast to move
fps = 40        # frame rate
afps = 4        # animation cycles
clock = pygame.time.Clock()
main = True

pygame.init()
screen = pygame.display.set_mode([screenX,screenY])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropRect = screen.get_rect()
ledge_list = createWorld()
player = Player()
player.rect.x = 199
player.rect.y = 40
movingsprites = pygame.sprite.Group()
movingsprites.add(player)

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
                player.jump(ledge_list)
#            if event.key == pygame.K_DOWN or event.key == ord('s'):
#                player.control(0,5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(movesteps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-movesteps,0)
#            if event.key == pygame.K_UP or event.key == ord('w'):
#                player.control(0,movesteps)
#            if event.key == pygame.K_DOWN or event.key == ord('s'):
#                player.control(0,-movesteps)
            # quitwatch
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    # scroll the world forward
    if player.rect.x >= forwardX:
        scroll = player.rect.x - forwardX
        player.rect.x = forwardX
        for platform in ledge_list:
            platform.rect.x -= scroll

    # scroll the world backward
    if player.rect.x <= backwardX:
        scroll = backwardX - player.rect.x
        player.rect.x = backwardX
        for platform in ledge_list:
            platform.rect.x += scroll

#    screen.fill(black)
    screen.blit(backdrop, backdropRect)
    ledge_list.draw(screen)
    player.gravity()
    #player.update(ledge_list)
    movingsprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
