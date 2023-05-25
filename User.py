class User(object):
    '''Пользователь, работающий в системе'''

    def __init__(self, user_id: int, group_id: int, 
                 user_name: str, priority: int):
        '''Создание нового пользователя'''
        self.user_id = user_id
        self.group_id = group_id
        self.user_name = user_name
        self.priority = priority # числа от 0 до 6
