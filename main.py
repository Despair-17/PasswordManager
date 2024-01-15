from database import Connection, Structure, ConnectionParameters, DatabaseService
from database.connection import psycopg2
from user_management import Registration, Authentication

# print(dir())
#
param = ConnectionParameters()
#
# reg = Registration('user0', 'password123A')
# reg.create_account()

# b'$2b$12$zNQ3VIyQFZt7FLWo59POuu' 29
# b'$2b$12$zNQ3VIyQFZt7FLWo59POuu4Ij7iLFMc5PXKrdLpouZ66QCk/C4une' 60

# with Structure(*param.fields) as structure:
#     structure.create_tables()

# with Structure(*param.fields) as structure:
#     structure.delete_table()
auth = Authentication('user1', 'password123A')
if auth.authenticate_account():
    print('Logged in successfully')
else:
    print('Wrong login or password')



# with DatabaseService(*param.fields) as cursor:
#     cursor.get_user_data('user1')

# for i in range(15, 100):
#     reg = Registration(f'user{i}', 'password123A')
#     reg.create_account()

# if __name__ == '__main__':
#     pass
'''Добавить систему логирования'''
