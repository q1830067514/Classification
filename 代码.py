# -*- coding: cp936 -*-
import linecache
o=open('四六级单词.csv')#文件路径
o.seek(0)
r=o.readlines()
s1=str(input('输入要定位的信息:'))
a=0
count=0
for i in r: #按和值组合查找
    if i.find(s1)>=0:       
        print(i)#显示定位行
        
    
