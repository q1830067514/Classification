=xx
# 只适用于英文文本
import re#导入模块
from string import punctuation

text = open('find.txt')#打开文件
text_list = text.readlines()
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
text_plain = re.sub(r'[{}]'.format(punctuation), '', ''.join(text_list))
one_word_list = [word.lower() for word in text_plain.split()]
print(one_word_list)#输出一个单词列表
def run_query(wanted):
    word_total = 0
    # 统计出现的总个数
    for each in one_word_list:
        if each == wanted:
            word_total += 1
    print('"{}" occurs {} times'.format(wanted, word_total))
    line_number = 0
    for line in text_list:#循环遍历列表
        line_plain = re.sub(r'[{}]'.format(punctuation), '', line)
        word_list = [word.lower() for word in line_plain.split()]
        # 按照用户习惯第一行从"1"开始
        line_number += 1#没循环一次加1
        # 每行的单词列表
        if wanted in word_list:
            # 而下标"0"表示第一行，故需要减去1
            print('\tline {}: {}'.format(line_number, text_list[line_number - 1]), end='')
if __name__ == '__main__':#调用主函数
    while True:
        sought = input('Input a word you want to search: ')
        if sought == 'q':
            break#跳出循环
        run_query(sought)
