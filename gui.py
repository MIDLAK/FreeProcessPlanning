from tkinter import IntVar, StringVar, Tk, Text, BOTH, X, N, LEFT
from tkinter.ttk import Combobox, Frame, Style, Label, Entry, Button, Spinbox
from loguru import logger

from User import User
from processManager import ProcessManager

# настройка логирования
logger.add('../logs/gui.log', format='{time} {level} {message}',
           level='DEBUG', rotation='10 MB', compression='zip')

class MainFrame(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Справедливое планирование')
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        # поля для ввода, кнопки, надписи
        user_lbl = Label(frame1, text='Пользователь', width=12)
        user_lbl.pack(side=LEFT, padx=5, pady=5)
        user_name_ent = Entry(frame1, width=50)
        user_name_ent.pack(side=LEFT, padx=5)
        user_name_btn = Button(frame1, text='Добавить', width=10)
        user_name_btn.pack(side=LEFT, padx=5)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        priority_lbl = Label(frame2, text='Приоритет', width=12)
        priority_lbl.pack(side=LEFT, padx=5, pady=5)
        priorities = ['0', '1', '2', '3', '4', '5', '6']
        priority_cmb = Combobox(frame2, values=priorities, 
                                width=48,
                                state='readonly')
        priority_cmb.current(1)
        priority_cmb.pack(side=LEFT, padx=5)
        priority_btn = Button(frame2, text='Установить', width=10)
        priority_btn.pack(side=LEFT, padx=6)

        frame3 = Frame(self)
        frame3.pack(fill=X)
        process_lbl = Label(frame3, text='Процесс', width=12)
        process_lbl.pack(side=LEFT, padx=5, pady=5)
        process_ent = Spinbox(frame3, width=47,
                              from_=0, to=100)
        process_ent.pack(side=LEFT, padx=5)
        process_btn = Button(frame3, text='Создать', width=10)
        process_btn.pack(side=LEFT, padx=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)
        quant_lbl = Label(frame4, text='Квант', width=12)
        quant_lbl.pack(side=LEFT, padx=5, pady=5)
        quant_ent = Entry(frame4, width=50)
        quant_ent.pack(side=LEFT, padx=5)
        quant_btn = Button(frame4, text='Принять', width=10)
        quant_btn.pack(side=LEFT, padx=5)



# параметры окна
main_window = Tk()
main_window.geometry('600x600+600+600')
app = MainFrame()
main_window.mainloop()
