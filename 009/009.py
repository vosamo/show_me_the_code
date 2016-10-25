#!/usr/bin/env python
# coding=utf-8
import urllib2
from bs4 import BeautifulSoup as BS

def find_all_link():
    links = []
    f = urllib2.urlopen('https://github.com/Show-Me-the-Code/show-me-the-code')
    text = BS(f, 'lxml')
    for link in text.find_all('a'):
        links.append(link['href'])
    return links


if __name__ == '__main__':
    print find_all_link()


