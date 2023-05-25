from enum import Enum

class ProccessStates(Enum):
    SUSPENSE = 0 # приостановка
    EXECUTION = 1  # исполнение
    COMPLETED = 2 # завершён

class Process(object):

    def __init__(self, process_id: int, user_id: int, 
                 state: ProccessStates, cpu: float, 
                 memory: float, time: float):
        self.process_id = process_id
        self.user_id = user_id
        self.state = state
        self.cpu = cpu
        self.memory = memory
        self.time = time
