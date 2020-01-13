'''
字符串和正则表达式
https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/12.%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%92%8C%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F.md
'''






'''
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
'''


import re

def main():
    username = input('请输入用户名: ')
    qq = input('请输入qq号: ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名')
    m2 = re.match(r'^[1-9]\d{4, 11}$', qq)
    if not m2:
        print('请输入有效的qq号')
    if m1 and m2:
        print('你输入的信息是有效的')




def match_phone():
    ''' 匹配手机号'''

    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，不是15600998765，也是110或119，王大锤的手机号才是15600998765。'
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())




def match_replay():
    '''替换字符串中的不良内容'''
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
    print(purified)



def match_split():
    '''拆分长字符串'''
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == '__main__':
    # main()
    # match_phone()
    # match_replay()
    match_split()