from tkinter import IntVar, StringVar, Tk, Text, BOTH, X, N, LEFT, RIGHT
from tkinter.ttk import Combobox, Frame, Style, Label, Entry, Button, Spinbox
from loguru import logger

from User import User
from Process import Process
from processManager import ProcessManager

# настройка логирования
logger.add('../logs/gui.log', format='{time} {level} {message}',
           level='DEBUG', rotation='10 MB', compression='zip')

class MainFrame(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.processes = []
        self.users = []

    def initUI(self):
        self.master.title('Справедливое планирование')
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        # поля для ввода, кнопки, надписи
        self.user_lbl = Label(frame1, text='Пользователь', width=12)
        self.user_lbl.pack(side=LEFT, padx=5, pady=5)
        self.user_name_ent = Entry(frame1, width=50)
        self.user_name_ent.pack(side=LEFT, padx=5)
        self.user_name_btn = Button(frame1, text='Добавить', width=10,
                                    command=self.create_user)
        self.user_name_btn.pack(side=LEFT, padx=5)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        self.priority_lbl = Label(frame2, text='Приоритет', width=12)
        self.priority_lbl.pack(side=LEFT, padx=5, pady=5)
        priorities = ['0', '1', '2', '3', '4', '5', '6']
        self.priority_cmb = Combobox(frame2, values=priorities, 
                                width=48,
                                state='readonly')
        self.priority_cmb.current(1)
        self.priority_cmb.pack(side=LEFT, padx=5)
        self.priority_btn = Button(frame2, text='Установить', width=10)
        self.priority_btn.pack(side=LEFT, padx=6)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        self.process_lbl = Label(frame3, text='Процесс', width=12)
        self.process_lbl.pack(side=LEFT, padx=5, pady=5)
        self.process_ent = Spinbox(frame3, width=47,
                              from_=0, to=100)
        self.process_ent.pack(side=LEFT, padx=5)
        self.process_btn = Button(frame3, text='Создать', width=10)
        self.process_btn.pack(side=LEFT, padx=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        self.quant_lbl = Label(frame4, text='Квант', width=12)
        self.quant_lbl.pack(side=LEFT, padx=5, pady=5)
        self.quant_ent = Entry(frame4, width=50)
        self.quant_ent.pack(side=LEFT, padx=5)
        self.quant_btn = Button(frame4, text='Принять', width=10)
        self.quant_btn.pack(side=LEFT, padx=5)


    def create_user(self) -> User:
        '''По имени из user_name_ent создаёт нового пользователя
        и добавляет его в список users'''
        user_name = self.user_name_ent.get()

        # поиск свободного id для нового пользователя
        free_id = 1
        if len(self.users) != 0:
            for user in self.users:
                if user.user_id > free_id:
                    free_id = user.user_id + 1

        priority = int(self.priority_cmb.get())
        user = User(user_name=user_name, user_id=free_id, 
                               priority=priority, group_id=1)
        self.users.append(user)
        logger.info(f'Пользователь {user_name} создан (id = {free_id}, priority = {priority}')
        return user

# параметры окна
main_window = Tk()
main_window.geometry('600x600+600+600')
app = MainFrame()
main_window.mainloop()
