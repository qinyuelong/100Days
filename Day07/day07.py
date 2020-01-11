'''

https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/07.%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%92%8C%E5%B8%B8%E7%94%A8%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.md

'''



s1 = 'abc12'

print(s1[-3: -1])


print(s1.center(50, "*"))

print(s1.isdigit()) # 是否已数字构成
print((s1.isalpha())) # 是否以字母构成
print(s1.isalnum()) # 是否以数字和字母构成
print(s1.strip()) # 修剪左右两侧的空格


# 格式化输出
a, b, = 5, 10
print('{0} * {1} = {2}'.format(a,b, a * b))

print(f'{a} * {b} = {a * b}')



import os
import time

def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.9)
        content = content[1: ] + content[0]




import random

def generate_code(code_len=4):
    '''
    生成指定长度的验证码
    :param code_len: 验证码长度默认4
    :return: 由大小写英文字母和数字构成的随即验证码
    '''

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code




def get_suffix(filename, has_dot=False):
    '''
    获取文件名的后缀

    :param filename: 文件名
    :param has_dot: 返回的后缀是否需要带点
    :return:  文件后缀名
    '''
    pos = filename.rfind('.')
    if 0 < pos < len(filename) -1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''




'''
设计一个函数返回传入的列表中最大和第二大的元素的值。
'''

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2



'''
计算指定的年月日是这一年的第几天。

'''


def is_leap_year(year):
    '''
    判断是不是闰年
    :param year: 年份
    :return: 闰年返回True 否则返回False
    '''
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0



def which_day(year, month, date):
    '''
    计算传入的日期是这一年的第几天

    :param year:
    :param month:
    :param date:
    :return:
    '''
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month-1):
        total += days_of_month[index]
    return total + date




'''

打印杨辉三角。
'''

def triangles():
    num = 5
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row -1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()



'''

双色球选号
双色球每注投注号码由6个红色球号码和1个蓝色球号码组成。
红色球号码从1--33中选择；蓝色球号码从1到16中选择。每注需要选择6个红色球号码，1个蓝色球号码
'''

from random import randrange, randint, sample

def display(balls):
    '''
    输出双色球的号码

    :param balls:
    :return:
    '''
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    '''随即选择一组号码'''
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def shuanse_game():
    n = 5
    for _ in range(n):
        display(random_select())






'''

约瑟夫环问题。
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，
由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，
问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。

'''

def yuesefu_circle():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end=' ')




'''

井字棋游戏。

'''

import os

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])



def shap_game():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋，请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局？（yes|no）')
        begin = choice == 'yes'


if __name__ == '__main__':
    # main()
    code = generate_code()
    print(code)

    file_subfix = get_suffix('test.txt')
    print(file_subfix)

    l = [1, 3, 8, 2, 6]
    r = max2(l)
    print(r)

    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))

    triangles()

    shuanse_game()

    yuesefu_circle()

    shap_game()