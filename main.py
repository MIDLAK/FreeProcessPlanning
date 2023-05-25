from User import User
from Process import Process, ProccessStates
from processManager import ProcessManager
from loguru import logger
from threading import Lock, Thread


@logger.catch
def main():
    process_manager = ProcessManager(memory=8000, quantum=0.01)
    # создание пользователей
    vadim = User(user_id=1, group_id=1, user_name='vadim', priority=0)
    regina = User(user_id=3, group_id=1, user_name='regian', priority=1)
    sofia = User(user_id=2, group_id=1, user_name='sofia', priority=3)

    process_manager.create_process(user=regina, time=1)
    process_manager.create_process(user=sofia, time=1)
    process_manager.create_process(user=sofia, time=1)

    pm_thread = Thread(target=process_manager.run, daemon=True)
    pm_thread.start()
    
    process_manager.create_process(user=sofia, time=1)
    process_manager.create_process(user=sofia, time=1)
    process_manager.create_process(user=sofia, time=1)
    process_manager.create_process(user=vadim, time=1)

    pm_thread.join()

if __name__ == '__main__':
    main()
