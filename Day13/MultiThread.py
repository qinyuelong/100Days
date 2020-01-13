import time
import tkinter
import tkinter.messagebox
from threading import Thread



def main():

    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成')
            button1.config(state=tkinter.NORMAL)


    def download():
        button1.config(state=tkinter.DISABLED)
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者： 骆昊')


    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()



from time import time
from random import randint
from multiprocessing import Process, Queue




def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def task_main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index: index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end-start), 's', sep=' ')


if __name__ == '__main__':
    # main()
    task_main()