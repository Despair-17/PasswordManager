import psycopg2


class Connection:

    def __init__(self, host: str, port: str, db_name: str, user: str, password: str):
        self._host = host
        self._port = port
        self._db_name = db_name
        self._user = user
        self._password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self._host,
                port=self._port,
                database=self._db_name,
                user=self._user,
                password=self._password
            )
            print('Successfully connected to the db PostgreSQL')
        except Exception as err:
            # Доработать этот момент
            print('Error while connecting to db PostgreSQL', err)

    def disconnect(self):
        try:
            self.connection.close()
            print('Disconnected from db PostgreSQL')
        except Exception as err:
            # Доработать этот момент
            print('Error while disconnecting', err)

    def connect_status(self):
        if self.connection is None or self.connection.closed:
            print('No connection to database')
        else:
            print('Connected to database')
