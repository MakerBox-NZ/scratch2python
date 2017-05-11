#!/usr/bin/env python
"""
Cheap stand-in for Image Magick `identify` 
by Klaatu

GNU All-Permissive License
--------------------------
Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.
http://gnu.org

Requires
--------
* Python 2.x or Python 3.x
* PIL (if python 2.x)
* Pillow (if python 3.x)
"""

from PIL import Image
import os.path
import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    sys.exit('Syntax: identify.py <filename>')

pic = sys.argv[1]
dim = Image.open(pic)
X   = dim.size[0]
Y   = dim.size[1]

print(X,Y)

