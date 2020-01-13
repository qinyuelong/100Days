from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('python.pdf', ))
    t1.start()
    t2 = Thread(target=download, args=('Peking hot.avi', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒' % (end - start))





class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成 耗费了%d秒' % (self._filename, time_to_download))



def download_main():
    start = time()
    t1 = DownloadTask('python.pdf')
    t1.start()
    t2 = DownloadTask('Peking hoc.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒' % (end - start))






'''
银行转账

'''

from threading import Thread, Lock

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()


    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()




    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)



def account_main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账号余额为： ¥%d元' % account.balance)




if __name__ == '__main__':
    # main()
    # download_main()
    account_main()