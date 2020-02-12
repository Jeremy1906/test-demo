# coding: utf-8
from tkinter import *
import re


class App:
    def __init__(self):
        self.label_show = ''
        self.point_onOff = True
        self.master = Tk()
        self.master.title('Tkinter Calc')
        wx = self.master.winfo_screenwidth()
        wy = self.master.winfo_screenheight()
        mw = self.master.winfo_reqwidth()
        mh = self.master.winfo_reqheight()
        self.master.geometry("%dx%d+%d+%d" % (mw, mh, (wx - mw) / 2, (wy - mh) / 2))
        self.master.resizable(width=False, height=False)
        self.init_widget()

    def show_command(self, event):
        enter_num = event.widget['text']

        # 判断当数字为0的时候，输入1-9替换0
        petten_notzero = re.compile(r'[1-9]')
        min_d = petten_notzero.findall(enter_num)

        if enter_num == 'C':
            self.label_show['text'] = '0'
            self.point_onOff = True
        elif self.label_show['text'] == '0' and min_d:
            self.label_show['text'] = enter_num
        elif enter_num == '.' and self.point_onOff:
            self.label_show['text'] += enter_num
            self.point_onOff = False
        elif enter_num == '/' or enter_num == '*' or enter_num == '+' or enter_num == '-':
            self.point_onOff = True
            if self.label_show['text'][-1] == '/' and enter_num == '/':
                pass
            elif self.label_show['text'][-1] == '*' and enter_num == '*':
                pass
            elif self.label_show['text'][-1] == '+' and enter_num == '+':
                pass
            elif self.label_show['text'][-1] == '-' and enter_num == '-':
                pass
            elif self.label_show['text'][-1] == '/' and (enter_num == '*' or enter_num == '+' or enter_num == '-'):
                self.label_show['text'] = self.label_show['text'][:-1] + enter_num
            elif self.label_show['text'][-1] == '*' and (enter_num == '/' or enter_num == '+' or enter_num == '-'):
                self.label_show['text'] = self.label_show['text'][:-1] + enter_num
            elif self.label_show['text'][-1] == '+' and (enter_num == '*' or enter_num == '/' or enter_num == '-'):
                self.label_show['text'] = self.label_show['text'][:-1] + enter_num
            elif self.label_show['text'][-1] == '-' and (enter_num == '*' or enter_num == '+' or enter_num == '/'):
                self.label_show['text'] = self.label_show['text'][:-1] + enter_num
            else:
                self.label_show['text'] += enter_num
        else:
            if self.point_onOff == False and enter_num == '.':
                pass
            else:
                self.label_show['text'] += enter_num

    def calc_command(self):
        """
        计算公式
        :return:
        """
        int_num = re.compile(r'\d+\.0')
        float_num = re.compile(r'\d+\.\d+')
        try:
            result = eval(self.label_show['text'])
            if int_num.findall(str(result)):
                result = int(result)
            elif float_num.findall(str(result)):
                result = float('%.3f' % result)
            self.label_show['text'] = str(result)
        except ValueError as e:
            print(e)
            self.label_show['text'] = 'ValueError'


    def init_widget(self):
        self.label_show = Label(self.master,
                                width=50,
                                font=("微软雅黑", 20),
                                text="0",
                                anchor=E,
                                relief=SUNKEN,
                                background="white")
        self.label_show.pack(side=TOP, fill=X, pady=3)

        frame = Frame(self.master)
        frame.pack(side=TOP)

        keys = ("7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "+",
                ".", "0", "C", "-")

        for i in keys:
            b_key = Button(frame, text=i, width=3)
            b_key.grid(row=int(keys.index(i) / 4), column=int(keys.index(i) % 4))
            b_key.bind("<Button-1>", self.show_command)

        equal = Button(frame, text="=", width=10, command=self.calc_command)
        equal.grid(row=4, column=2, columnspan=2)

        self.master.bind("<Escape>", lambda e: self.master.destroy())
        self.master.mainloop()


if __name__ == "__main__":
    App()
