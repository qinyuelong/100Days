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


c_mn()