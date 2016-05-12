#!/usr/bin/env python
# coding=utf-8
import random
import MySQLdb as MS
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
    conn = MS.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='271828',
            db='test')
    cur = conn.cursor()
    #sql = 'create table code (id int AUTO_INCREMENT,code varchar(20),primary key(id))'
    #cur.execute(sql)
    for cd in codes:
        cur.execute('insert into code (code) values ("' + cd + '")')
    cur.close()
    conn.commit()
    conn.close()
if __name__ == '__main__':
    codes = genNum(200,10)
    saveCode(codes)
