class User(object):
    '''Пользователь, работающий в системе'''

    def __init__(self, user_id: int, group_id: int, 
                 user_name: str, promised_cpu: float):
        '''Создание нового пользователя'''
        self.user_id = user_id
        self.group_id = group_id
        self.user_name = user_name
        self.promised_cpu = promised_cpu
