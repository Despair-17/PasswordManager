from database import Connection, Structure, ConnectionParameters, DatabaseService
from database.connection import psycopg2
from security import Encryption

print(dir())
#
param = ConnectionParameters()
# struct = Structure(**param.__dict__)
# struct.create_tables()
# struct.disconnect()

service = DatabaseService(**param.__dict__)
for i in range(10):
    service.add_user_data(f'user{i}', 'password')

service.disconnect()
# if __name__ == '__main__':
#     pass
