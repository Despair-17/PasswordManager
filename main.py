from database import Connection, Structure, ConnectionParameters, UserService, PasswordService
from database.connection import psycopg2
from user_management import Registration, Authentication
from random import shuffle
from password_management import PasswordManager

# print(dir())
#
param = ConnectionParameters()

# reg = Registration('user0', 'password123A')
# reg.create_account()

# with Structure(*param.fields) as structure:
#     # structure.delete_table()
#     structure.create_tables()

# for i in range(1, 10):
#     reg = Registration(f'user{i}', 'password123A')
#     reg.create_account()
#
# with PasswordManager() as cursor:
#     # password = list('Heso0601yam')
#     for i in range(1, 10):
#         for j, value in enumerate(['yandex.ru', 'google.com', 'facebook.com', 'twitter.com']):
#             # shuffle(password)
#             cursor.add_password(i, value, f'login{j}', 'Heso0601yam', 'Да да я')
# #
# with PasswordManager() as cursor:
#     print(cursor.gen_password())
#     # cursor.update_password(1, 'facebook.com', 'login2', 'aezakmi8342')
#     cursor.delete_password(1, 'facebook.com', 'login2')
#     print(*cursor.get_passwords(1), sep='\n')

# auth = Authentication('user1', 'password123A')
# user_id, flag = auth.authenticate_account()
# if flag:
#     print('Logged in successfully')
# else:
#     print('Wrong login or password')

# if __name__ == '__main__':
#     pass
'''Добавить систему логирования'''
