# 查询文本中某单词出现的次数，并打印其出现的行号及所在行的内容
# 只适用于英文文本
import re
from string import punctuation
text = open('find.txt')
text_list = text.readlines()
# 删除标点符号及其他常用符号
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
text_plain = re.sub(r'[{}]'.format(punctuation), '', ''.join(text_list))
# 转换为小写，便于正确统计单词数
one_word_list = [word.lower() for word in text_plain.split()]
print(one_word_list)
def run_query(wanted):
    word_total = 0
    for each in one_word_list:
        if each == wanted:
            word_total += 1
  print('"{}" occurs {} times'.format(wanted, word_total))
   line_number = 0
    for line in text_list:
        line_plain = re.sub(r'[{}]'.format(punctuation), '', line)
        word_list = [word.lower() for word in line_plain.split()]
        # 按照用户习惯第一行从"1"开始
        line_number += 1     # 每行的单词列表
        if wanted in word_list:   # 而下标"0"表示第一行，故需要减去1
            print('\tline {}: {}'.format(line_number, text_list[line_number - 1]), end='')
if __name__ == '__main__':#作用是控制这两种情况执行代码的过程，在if __name__ == 'main': 下的代码只有文件作为脚本直接执行才会被执行，而import到其他脚本中是不会被执行的。
    while True:
        sought = input('Input a word you want to search: ')
        if sought == 'q':
            break
run_query(sought) #开始查询
