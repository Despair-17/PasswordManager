from database import Connection, Structure, ConnectionParameters, DatabaseService
from database.connection import psycopg2
from user_management import Registration

# print(dir())
#
param = ConnectionParameters()

reg = Registration('User13', 'password')
reg.create_account()

# conn = Connection(*param.fields)
#
#
# conn._connect()
# conn._disconnect()

# with Structure(**param.fields) as structure:
#     structure.create_tables()
#
# with DatabaseService(*param.fields) as service:
#     service.add_user_data(f'user0', 'password')

# if __name__ == '__main__':
#     pass
'''Добавить систему логирования'''

# from exceptions import LoginExistsError
#
#
# class Test:
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_val, 1)
#         if isinstance(exc_val, LoginExistsError):
#             return False
#         return True
#
#     def method(self):
#         try:
#             raise Exception('Method error')
#         except Exception as err:
#             raise LoginExistsError('Castom error') from err
#
#
# class Test2:
#
#     def method2(self):
#         with Test() as test:
#             try:
#                 test.method()
#             except LoginExistsError as err:
#                 print(err, 2)
#         # try:
#         #     with Test() as test:
#         #         test.method()
#         # except LoginExistsError as err:
#         #     print(err, 2)
#
#
# a = Test2()
# a.method2()
