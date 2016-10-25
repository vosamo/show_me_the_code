#!/usr/bin/env python
# coding=utf-8
import urllib2
from bs4 import BeautifulSoup as BS

f = urllib2.urlopen('https://github.com/Show-Me-the-Code/show-me-the-code')
text = BS(f, 'lxml')

content = text.get_text().strip('\n')
print content


