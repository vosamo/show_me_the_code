#!/usr/bin/env python
# coding=utf-8
from PIL import Image, ImageDraw, ImageFont
def addNum(imgName):
    img = Image.open(imgName)
    drawImg = ImageDraw.Draw(img)
    
    w, h = img.size
    fontSize = min(w,h)/9
    
    myFont = ImageFont.truetype('ARIAL.TTF',fontSize)
    drawImg.text((0.9*w,0.08*h), "5", fill=(255,0,0),font=myFont)
    img.save('000_new.jpg','jpeg')
    img.show()
if __name__ == '__main__':
    addNum('000.jpg')
