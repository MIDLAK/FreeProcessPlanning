from User import User
from Process import Process, ProccessStates
from processManager import ProcessManager
from loguru import logger
from threading import Lock, Thread

process_manager = ProcessManager(memory=8000, quantum=1)

@logger.catch
def main():
    # создание пользователей
    vadim = User(user_id=1, group_id=1, user_name='vadim', promised_cpu=50.0)
    regina = User(user_id=3, group_id=1, user_name='regian', promised_cpu=50.0)
    sofia = User(user_id=2, group_id=1, user_name='sofia', promised_cpu=50.0)

    process_manager.create_process(user_id=regina.user_id, time=4)

    pm_thread = Thread(target=process_manager.run, daemon=True)
    pm_thread.start()

    process_manager.create_process(user_id=sofia.user_id, time=10)
    process_manager.create_process(user_id=sofia.user_id, time=5)
    process_manager.create_process(user_id=sofia.user_id, time=16)
    process_manager.create_process(user_id=sofia.user_id, time=1)
    process_manager.create_process(user_id=sofia.user_id, time=1)
    process_manager.create_process(user_id=sofia.user_id, time=3)

    pm_thread.join()

if __name__ == '__main__':
    main()
