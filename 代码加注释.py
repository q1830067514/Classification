# -*- coding:utf-8 -*-
import linecache  #导入模块
o=open('单词表.csv')#文件路径
o.seek(0)   #指针指向第一的
r=o.readlines()  #读取一行
s1=str(input('输入要定位的信息:'))   #请输入要定位的信息
a=0   #初始化a
count=0





for i in r: #按和值组合查找
    if i.find(s1)>=0:       
        print(i )     #显示定位行
print ('Total:%d'%count)      #输出
