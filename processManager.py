from Process import Process, ProccessStates
from time import sleep
from loguru import logger
from threading import Lock, Thread

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


    def create_process(self, user_id: int, time: float) -> Process | ValueError:
        '''Запрос на создание пользователем с идентификатором 
        user_id процесса с временем выполнения time '''
        if self.__is_resources(time) == False:
            logger.error(f'Недостаточно ресурсов для создания процесса user_id = {user_id}')
            return ValueError('Недостаточно ресурсов')

        # создание нового процесса
        free_pid = self.__free_pid()
        sleep(1) # время на создание процесса
        process = Process(process_id=free_pid, user_id=user_id,
                          state=ProccessStates.SUSPENSE, cpu=0.0,
                          memory=0.0, time=time)
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
                process.state = ProccessStates.EXECUTION
                logger.debug(f'Процесс pid = {process.process_id} выполняется')
                sleep(self.quantum)
                process.time = process.time - self.quantum

                # проверка на завершение выполнения процесса
                if process.time <= 0:
                    process.state = ProccessStates.COMPLETED
                    logger.info(f'Процесс pid = {process.process_id} выполнен')
                    self.process_list.remove(process)

                process.state = ProccessStates.SUSPENSE
