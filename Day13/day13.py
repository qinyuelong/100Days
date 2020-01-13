'''
https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/13.%E8%BF%9B%E7%A8%8B%E5%92%8C%E7%BA%BF%E7%A8%8B.md
'''


from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s..' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (filename, time_to_download))



def main():
    start = time()
    download_task('python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒' % (end-start))


if __name__ == '__main__':
    main()