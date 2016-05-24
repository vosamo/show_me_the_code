#!/usr/bin/env python
# coding=utf-8
import Image
import os

IPHONE5_WIDTH = 1136
IPHONE5_HEIGHT = 640
def resizePic(path, newPath, width=IPHONE5_WIDTH, height=IPHONE5_HEIGHT):
    img = Image.open(path)
    w, h = img.size
    if w > width:
        h = h*height/w
        w = width
    if h > height:
        w = w*width/h
        h = height
    smallImg = img.resize((w,h),Image.ANTIALIAS)
    smallImg.save(newPath)

def resizePics(path):
    for root, dirs, files in os.walk(path):
        for fname in files:
            if fname.lower().endswith('jpg'):
                dstPath = os.path.join(root,fname)
                newName = 'iphone5_' + fname
                resizePic(dstPath,newName)

if __name__ == '__main__':
    resizePics('./')
