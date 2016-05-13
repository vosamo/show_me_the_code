#!/usr/bin/env python
# coding=utf-8
import random
from redis import Redis

def genNum(num, len):
    """
    Generate a number of random code with length len.
    """
    seed = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    codeList = []
    for i in range(num):
        codeList.append(''.join(random.sample(seed, len)))
    return codeList

def saveCode(codes):
    r = Redis(host='localhost',port=6379,db=0)
    for code in codes:
        r.rpush('codes',code)
    r.save()
    #for code in r.lrange('codes',0,-1):
        #print code

if __name__ == '__main__':
    saveCode(genNum(200,10))
