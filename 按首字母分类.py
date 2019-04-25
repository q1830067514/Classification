#coding=utf-8
'''
边遍历，边构造 key value 
'''
lexicons=["the","be","of","and","A","to","in","he","have","it","that","for","they","I","with","as","not","on","she","at","by","this","we","you","do","but","from","or","which","one","would","all","will","there","say","who","make","when","can"]
lexiconDict={}
#分类  保存字典中
lexiconLen=len(lexicons)
for x in xrange(len(lexicons)):
    lexicon=lexicons[x]
    startLetter=lexicon[0]
    dictLexicons=lexiconDict.get(startLetter,[])
                #空列表说明没有Key 则添加Key 否则追加Key对应的Value
    if len(dictLexicons)==0:
        lexiconDict[startLetter]=[lexicons[x]]
    else:
        dictLexicons.append(lexicons[x])
while True:
    startLetter=raw_input("输入一个字母，列出所有以此字母开头的单词:")
    if len(startLetter)!=1:
        print "必须是一个字母"
    else:
        lexicons=lexiconDict.get(startLetter.lower(),[])
        if len(lexicons)==0:
            print "没有结果"
        else:
            for x in lexicons:
                print x
