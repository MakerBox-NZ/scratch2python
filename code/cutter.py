#!/usr/bin/env python

"""
This is klaatu's modified version of | 
Radomir Dopieralski's tilemap slicer |
-------------------------------------d

                           BSD LICENSE

Copyright (c) 2008, 2009, Radomir Dopieralski
All rights reserved. 

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

 * Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in
   the documentation and/or other materials provided with the
   distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import pygame
import pygame.locals
from PIL import Image
import os.path
import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    sys.exit('O.o --> You must provide the filename of the tilemap you want to slice, and the tilesize by which you wish to divide. Example: cutter.py foo.png 32')

tilesize = int(sys.argv[2])
# determine original size of image before cutting
tilemap = sys.argv[1]
#tilemap = os.path.abspath("/media/ixsystems/sxe/pygame/freeGameArt/Kenney/Platformer Pack/tiles_spritesheet.png")
dimensions = Image.open(tilemap)
screenX = dimensions.size[0]
screenY = dimensions.size[1]

def load_tile_table(filename, width, height):
    image = pygame.image.load(tilemap).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width/width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height/height):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((screenX+screenX/tilesize, screenY+screenY/tilesize))
    screen.fill((255, 255, 255))
    table = load_tile_table(tilemap, tilesize, tilesize)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*(tilesize+1), y*(tilesize+1)))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass
