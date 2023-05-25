from Process import Process, ProccessStates
from User import User
from time import sleep
from loguru import logger


import matplotlib.pyplot as plt

# настройка логирования
logger.add('../logs/process_manager.log', format='{time} {level} {message}',
           level='DEBUG', rotation='10 MB', compression='zip')

class ProcessManager(object):
    '''Менеджер процессов отвечет за создание процессов и принятия решений
    об их исполнении'''

    def __init__(self, memory: float, quantum: float):
        self.cpu = 100.0
        self.memory = abs(memory)
        self.memory_use = 0.0
        self.cpu_use = 0.0
        self.process_list = []
        self.quantum = abs(quantum) # квантум времени в секундах


    def create_process(self, user: User, time: float) -> Process | ValueError:
        '''Запрос на создание пользователем с идентификатором 
        user_id процесса с временем выполнения time '''
        if self.__is_resources(time) == False:
            logger.error(f'Недостаточно ресурсов для создания процесса user_id = {user.user_id}')
            return ValueError('Недостаточно ресурсов')

        # создание нового процесса
        free_pid = self.__free_pid()
        sleep(0.5) # время на создание процесса
        process = Process(process_id=free_pid, user=user,
                          state=ProccessStates.SUSPENSE, cpu=0.0,
                          memory=0.0, time=time)
        # распределение процесса в сооветвующую приоритетную группу
        self.process_list.append(process)
        logger.info(f'Процесс pid = {process.process_id} создан')
        return process 

    
    def __is_resources(self, time) -> bool:
        '''Проверка наличия ресурсов на создание процесса'''
        if self.cpu_use == 100.0 \
                or self.memory_use == self.memory \
                or time >= 1000:
            return False
        else:
            return True


    def __free_pid(self) -> int:
        '''Возвращает свободный идентификатор процесса'''
        free_pid = 1
        if len(self.process_list) != 0:
            max_pid = 1
            for process in self.process_list:
                if process.process_id > max_pid:
                    max_pid = process.process_id
            free_pid = max_pid + 1
        return free_pid
    

    def run(self):
        '''Запускается выполнение процессов из очереди'''
        while True:
            for process in self.process_list:
                counter = 0
                for _ in range(2**(6 - process.user.priority)):
                    process.state = ProccessStates.EXECUTION

                    # если процессу нужно меньше времени чем предполагает квант
                    if process.time < self.quantum:
                        sleep(process.time)
                    else:
                        sleep(self.quantum)
                    process.time = process.time - self.quantum
                    counter = counter + 1

                    # проверка на завершение выполнения процесса
                    if process.time <= 0:
                        process.state = ProccessStates.COMPLETED
                        logger.info(f'Процесс pid = {process.process_id} выполнен')
                        self.process_list.remove(process)
                        break
                    process.state = ProccessStates.SUSPENSE
                    
                logger.debug(f'Процесс pid = {process.process_id} выполняется {counter} раз')

