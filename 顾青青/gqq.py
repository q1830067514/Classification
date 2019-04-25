#20161152158 顾青青

#-*-coding:utf-8-*-
import codecs
import json
import os
import string
import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet
from datetime import datetime
import multiprocessing

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
path = sys.path[0]

class NlpPreProcess(object):
    def __init__(self, stopfile, downlist):
        super(NlpPreProcess, self).__init__()
        self.wnl = WordNetLemmatizer() # 词形还原
        self.ps = PorterStemmer() # 词干提取
        with codecs.open(stopfile, 'r', 'utf-8') as f:
            self.stoplist = f.read().splitlines()
        print ('the num of stopwords is %s'%len(self.stoplist))
        self.downlist = downlist # 文件夹下已经处理过的文档，避免重复抓取
        self.allnum = 0

    def preprocess_folder(self, source_folder, dest_folder):
        stime = datetime.now()
        for filename in os.listdir(source_folder):
            self.preprocess_file(filename, source_folder, dest_folder)
        print ('the num of all valid docs is : %s'%self.allnum)

    def preprocess_folder_multiprocess(self, source_folder, dest_folder, process_num):
        filelist = os.listdir(source_folder)
        tmp = []
        process_list = []
        num = 0
        for i in range(len(filelist)):
            i += 1
            if 'docwords'+filelist[i-1] in downlist: # 如果已处理则跳过
                continue
            tmp.append(filelist[i-1])
            num += 1
            if num%process_num == 0 or i==len(filelist):
                print ("the %dth loop"%(num/process_num))
                print ('------'*20)
                for filename in tmp:
                    process_list.append(multiprocessing.Process(target=self.preprocess_file, args=(filename, source_folder, dest_folder)))
                for p in process_list:
                    p.start()
                for p in process_list:
                    p.join()
                tmp = []
                process_list = []
        print ('the num of all valid docs is : %s'%self.allnum)

    def preprocess_file(self, filename, source_folder, dest_folder):
        '''去标点, 去数字, 分割成单词, 词形还原'''
        saveFileName = 'docwords'+filename[-1]
        if saveFileName in self.downlist:
            return 0
        print ('begin process %s'%filename)
        save_file = codecs.open(dest_folder + os.sep + saveFileName, 'w', 'utf-8')
        num = 0
        stime = datetime.now()
        for dic in self.generate_dict_from_file(source_folder + os.sep + filename):
            doc = dic['content'].lower()
            for c in string.punctuation: #去标点
                doc = doc.replace(c, ' ')
            for c in string.digits: #去数字
                doc = doc.replace(c, '')
            doc = nltk.word_tokenize(doc) #分割成单词
            # 只保留特定词性单词, 如名词
            # filter = nltk.pos_tag(doc)
            # doc = [w for w, pos in filter if pos.startswith("NN")]
            cleanDoc = []
            # 只保留长度不小于3的单词,去除停用词,验证是否为英文单词(利用wordnet)
            for word in doc:
                if len(word) >= 3 and word not in self.stoplist and wordnet.synsets(word):
                    word = self.wnl.lemmatize(word) #词形还原
                    #word = self.ps.stem(word) # 词干提取
                    cleanDoc.append(word)
            dic['content'] = ' '.join(cleanDoc)
            json.dump(dic, save_file, ensure_ascii=False)
            save_file.write('\n')
            num += 1
        print ('time cost is : %s'%(datetime.now()-stime))
        print ('the num of valid docs is : %s'%num)
        print ('---'*20)
        self.allnum += num
        return num

    def generate_dict_from_file(self, filename):
        """读取json文件，返回字典数据"""
        with codecs.open(filename, 'r', 'utf-8') as source_file:
            for line in source_file:
                try:
                    dic = json.loads(line.strip())
                    yield dic
                except:
                    pass

if __name__ == '__main__':
    source_folder = path + os.sep + 'cleanHtml'
    dest_folder = path + os.sep + 'docword'
    stopword_filepath = path + os.sep + 'stoplist.csv'
    process_num = 6 # 设置多进程数量
    downlist = os.listdir(dest_folder)
    nlp_preprocess = NlpPreProcess(stopword_filepath, downlist)
    nlp_preprocess.preprocess_file('sogou.json', source_folder, dest_folder)
    
