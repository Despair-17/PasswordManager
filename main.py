from database import Connection, Structure, ConnectionParameters, DatabaseService
from database.connection import psycopg2
from user_management import Registration, Authentication
from random import shuffle

# print(dir())
#
param = ConnectionParameters()
#
# reg = Registration('user0', 'password123A')
# reg.create_account()

# b'$2b$12$zNQ3VIyQFZt7FLWo59POuu' 29
# b'$2b$12$zNQ3VIyQFZt7FLWo59POuu4Ij7iLFMc5PXKrdLpouZ66QCk/C4une' 60

# with Structure(*param.fields) as structure:
#     # structure.delete_table()
#     structure.create_tables()
#
# for i in range(1, 10):
#     reg = Registration(f'user{i}', 'password123A')
#     reg.create_account()

# with DatabaseService(*param.fields) as cursor:
#     password = list('Heso0601yam')
#     for i in range(1, 10):
#         for j, value in enumerate(['yandex.ru', 'google.com', 'facebook.com', 'twitter.com']):
#             shuffle(password)
#             service_id = cursor.get_or_insert_service_id(value)
#             cursor.insert_password(i, service_id, f'login{j}', ''.join(password), 'Да да я')

# auth = Authentication('user1', 'password123A')
# if auth.authenticate_account():
#     print('Logged in successfully')
# else:
#     print('Wrong login or password')


# if __name__ == '__main__':
#     pass
'''Добавить систему логирования'''
