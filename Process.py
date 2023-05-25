from enum import Enum
from dataclasses import dataclass

class ProccessStates(Enum):
    SUSPENSE = 0    # приостановка
    EXECUTION = 1   # исполнение
    COMPLETED = 2   # завершён

@dataclass
class Process:
    process_id: int         # идентификатор процесса
    user_id: int            # идентификатор пользователя
    state: ProccessStates   # состояние процесса
    cpu: float              # использование процессом ресурсов ЦП
    memory: float           # использование процессом памяти
    time: float             # время, необходимое на вполнение процесса
