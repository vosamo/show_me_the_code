#!/usr/bin/env python
# coding=utf-8
import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255, 255, 255)
Image_Font = 'FreeSerif.ttf'
text = ' '.join(random.sample(string.digits + string.lowercase, 4))

def random_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def create_verify_code(strs, width=400, height=200, chance=2):
    im = Image.new(IMAGE_MODE, (width, height), IMAGE_BG_COLOR)
    draw = ImageDraw.Draw(im)
    # 绘制干扰背景
    for w in xrange(width):
        for h in xrange(height):
            if chance < random.randint(1, 100):
                draw.point((w, h), fill=random_color())

    font = ImageFont.truetype(Image_Font, 80)
    font_width, font_height = font.getsize(strs)
    strs_len = len(strs)
    x = (width - font_width)/2
    y = (height - font_height)/2
    # 绘制文字
    for str in strs:
        draw.text((x,y), str, random_color(), font)
        x += font_width/strs_len
    # 模糊处理
    # im = im.filter(ImageFilter.BLUR)
    im.save('identifying_code_pic.jpg')

if __name__ == '__main__':
    create_verify_code(text)
