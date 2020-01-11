'''

https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/06.%E5%87%BD%E6%95%B0%E5%92%8C%E6%A8%A1%E5%9D%97%E7%9A%84%E4%BD%BF%E7%94%A8.md
'''


'''

输入M和N计算C(M,N)
'''


def c_mn():
    m = int(input('m = '))
    n = int(input('n = '))
    fm = 1
    for num in range(1, m + 1):
        fm *= num
    fn = 1
    for num in range(1, n + 1):
        fn *= num
    fmn = 1
    for num in range(1, m - n + 1):
        fmn *= num
    print(fm // fn // fmn)


# c_mn()



def gcd(x, y):
    '''最大公约数'''
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor



def lcm(x, y):
    '''求最小公倍数'''
    return x * y // gcd(x, y)



'''

实现判断一个数是不是回文数的函数。

'''

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


'''
素数
指在大於1的自然数中，除了1和該数自身外，無法被其他自然数整除的数
'''

def is_prime(num):
    '''判断是不是素数'''
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False



if __name__ == '__main__':
    # num = int(input('请输入正整数: '))
    for num in range(1, 1000):
        if is_palindrome(num) and is_prime(num):
            print('%d 是回文素数' % num)

