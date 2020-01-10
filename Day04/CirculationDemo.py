

'''
https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/04.%E5%BE%AA%E7%8E%AF%E7%BB%93%E6%9E%84.md

'''


'''
https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/04.%E5%BE%AA%E7%8E%AF%E7%BB%93%E6%9E%84.md
'''

sum = 0
for x in range(2, 101, 2):
    print(x)
    sum += x
print(sum)




'''
输出乘法口诀表(九九表)

'''

for i in range(1, 10):
    for j in range(1, i+1):
        print('%d * %d = %d' % (j, i, i * j), end='\t')
    print()



''''
素数指的是只能被1和自身整除的大于1的整数。
输入一个正整数判断它是不是素数
'''

from math import sqrt

def calculPrime():
    num = int(input('请输入一个正整数: '))
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end+1):
        if num % x == 0:
            is_prime = False
            break

    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数 ' % num)



'''

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

'''

import random

def randomNumber():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了')
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')



'''

输入两个正整数，计算它们的最大公约数和最小公倍数。
'''

def calculTwoNumberFactor():
    x = int(input('x = '))
    y = int(input('y = '))
    if x > y:
        x, y = y ,x

    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d 和 %d 的最大公约数是 %d' % (x, y , factor))
            print('%d 和 %d 的最小公倍数是 %d' % (x, y, x * y // factor))
            break

# calculTwoNumberFactor()


def printShape():
    row = int(input('请输入行数: '))
    for i in range(row):
        for _ in range(i+1):
            print('*', end='')
        print()


    print()
    print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    print()
    print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


printShape()