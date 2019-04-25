#首字母小写分类
#coding=utf-8
lexicons=["the","be","of","and","a","to","in","he","have","it","that","for","they","I","with","as","not","on","she","at","by","this","we","you","do","but","from","or","which","one","would","all","will","there","say","who","make","when","can"]
while True:
    startLetter=raw_input("输入一个字母，列出所有以此字母开头的单词:")
    if len(startLetter)!=1:
        print "必须是一个字母"
    else:
        reLexicons=[] #结果列表
        for x in xrange(len(lexicons)):
            lexicon=lexicons[x]
            if lexicon[0].lower()==startLetter.lower():#都转为小写后比较  开头字母不区分大小写
                reLexicons.append(lexicon)
        if len(reLexicons)==0:
            print "没有结果"
        else:
            for x in xrange(len(reLexicons)):
                print reLexicons[x]
