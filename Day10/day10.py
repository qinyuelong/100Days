'''

https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/10.%E5%9B%BE%E5%BD%A2%E7%94%A8%E6%88%B7%E7%95%8C%E9%9D%A2%E5%92%8C%E6%B8%B8%E6%88%8F%E5%BC%80%E5%8F%91.md
'''


import tkinter
import tkinter.messagebox

def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!') if flag else ('blue', 'GoodBye, world!')
        label.config(text=msg, fg=color)


    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗？'):
            top.quit()

    top = tkinter.Tk()
    top.geometry('240x160')
    top.title('小游戏')
    label = tkinter.Label(top, text='Hello world', font='Arial -32', fg='red')
    label.pack(expand=1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()
