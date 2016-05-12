#!/usr/bin/env python
# coding=utf-8
import random
def genNum(num, len):
    """
    Generate a number of random code with length len.
    """
    seed = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(num):
        print ''.join(random.sample(seed, len))
if __name__ == '__main__':
    genNum(200,10)
