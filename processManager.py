from Process import Process, ProccessStates
from time import sleep
from loguru import logger
from threading import Lock, Thread

# настройка логирования
logger.add('../logs/process_manager.log', format='{time} {level} {message}',
           level='DEBUG', rotation='10 MB', compression='zip')

class ProcessManager(object):

    def __init__(self, memory: float, quantum: float):
        self.cpu = 100.0
        self.memory = memory
        self.memory_use = 0.0
        self.cpu_use = 0.0
        self.process_list = []
        self.quantum = quantum # квантум времени в секундах

    def create_process(self, user_id: int, time: float) -> Process | ValueError:
        '''Запрос на создание пользователем с идентификатором 
        user_id процесса с временем выполнения time '''
        if self.cpu_use == 100.0 \
                            or self.memory_use == self.memory or time >= 1000:
            logger.error(f'Недостаточно ресурсов для создания процесса user_id = {user_id}')
            return ValueError('Недостаточно ресурсов')

        free_pid = 1
        if len(self.process_list) != 0:
            max_pid = 1
            for process in self.process_list:
                if process.process_id > max_pid:
                    max_pid = process.process_id
            free_pid = max_pid + 1

        sleep(1) # время на создание процесса
        process = Process(process_id=free_pid, user_id=user_id,
                          state=ProccessStates.SUSPENSE, cpu=0.0,
                          memory=0.0, time=time)
        self.process_list.append(process)
        logger.info(f'Процесс pid = {process.process_id} создан и добавлен в очередь')
        return process 

    def run(self):
        '''Запускается выполнение процессов из очереди'''
        while True:
            for process in self.process_list:

                process.state = ProccessStates.EXECUTION

                logger.debug(f'Процесс pid = {process.process_id} выполняется')
                sleep(self.quantum)
                process.time = process.time - self.quantum
                if process.time <= 0:
                    process.state = ProccessStates.COMPLETED
                    logger.debug(f'Процесс pid = {process.process_id} выполнен и покидает очередь')
                    self.process_list.remove(process)

                process.state = ProccessStates.SUSPENSE


            
