from database import Connection, Structure, ConnectionParameters, DatabaseService
from database.connection import psycopg2
from security import Encryption

print(dir())
#


param = ConnectionParameters()
# conn = Connection(**param.__dict__)
# conn.connect()
# conn.disconnect()
# with Structure(**param.__dict__) as structure:
#     structure.create_tables()

with DatabaseService(**param.__dict__) as service:
    for i in range(10):
        service.add_user_data(f'user{i}', 'password')

# if __name__ == '__main__':
#     pass
