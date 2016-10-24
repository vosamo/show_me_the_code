#!/usr/bin/env python
# coding=utf-8
import os
import re

def walk_dir(dirPath):
    file_path = []
    for root, dirs, files in os.walk(dirPath):
        for f in files:
            if f.lower().endswith('.txt'):
                file_path.append(os.path.join(root, f))
    return file_path

def count_words(file_path):
    word_dict = {}
    filename = os.path.basename(file_path)
    with open(file_path) as f:
        text = f.read()
        word_list = re.findall(r'[a-zA-Z]+', text)
        for w in word_list:
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1
        sorted_word_list = sorted(word_dict.items(), key=lambda d:d[1])
        print u"在%s文件中，%s为关键字，出现次数为%s" % (filename, sorted_word_list[-1][0], sorted_word_list[-1][1])

if __name__ == "__main__":
    for file_path in walk_dir(os.getcwd()):
        count_words(file_path)
