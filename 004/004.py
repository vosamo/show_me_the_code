#!/usr/bin/env python
# coding=utf-8
"""
004题：统计一个纯英文文本文件中的单词个数
"""
import re

def count_words(fname):
    with open(fname) as f:
        text = f.read()
        word_list = re.findall(r'[a-zA-Z0-9]+',text)
    return len(word_list)

if __name__ == '__main__':
    print count_words('words.txt')
