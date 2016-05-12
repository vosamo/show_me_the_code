#!/usr/bin/env python
# coding=utf-8
"""
Cut,Rotate and paste an image.
"""
from PIL import Image
im = Image.open('./tx.jpg')
w, h = im.size
wLeft = w/2
boxLeft = (0,0,wLeft,h)
boxRight = (wLeft,0,w,h)
boxLeftNew = (0,0,w-wLeft,h)
boxRightNew = (w-wLeft,0,w,h)

# crop to cut a part,transpose to rotate or flip an image.
leftPart = im.crop(boxLeft).transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_180)
rightPart = im.crop(boxRight)

# paste to rebuild an image.
im.paste(rightPart, boxLeftNew)
im.paste(leftPart, boxRightNew)

im.show()
