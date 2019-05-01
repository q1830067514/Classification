#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import sys
import re
from bs4 import BeautifulSoup

URL = 'http://www.iciba.com/'

while True:
    try:
        word = raw_input("请输入你要查找的单词(或者按CTRL+D或CTRL+C退出):")
    except KeyboardInterrupt:
        print "\n退出。"
        sys.exit(1)
    except EOFError:
        print "\n退出。"
        sys.exit(1)
    if not word:
        break
    url = URL + word
    #查找单词
    f = urllib.urlopen(url)
    reader = f.readlines()
    #用正则表达式进行匹配
    #这里我用BeautifulSoup进行标签的解析
    soup = BeautifulSoup(''.join(reader))   #新建一个soup对象
    #先进行一般释义的抓取
    results1 = soup.findAll("div",{"class":"group_pos"})
    if not results1:
        print '不好意思，找不到你要查找的单词'
        continue
    #对每块进行解析
    sys.stdout.write('\n')   #换行
    for item in results1:
        aa = item.findAll("strong",{"class":"fl"})
        bb = item.findAll("span",{"class":"label_list"})
        #二重循环
        for i in range(len(aa)):
            print aa[i].contents[0],
            dd = bb[i].findAll("label")
            for ee in dd:
                print ee.contents[0],
            sys.stdout.write('\n') #分好行 
    #查找网络释义
    results2 = soup.findAll("div",{"class":"net_paraphrase"})
    print "网络释义:",
    ff = results2[0].findAll("li")
    for item in ff:
        print item.contents[0],
    sys.stdout.write('\n')   #换行
    sys.stdout.write('\n')   #换行
