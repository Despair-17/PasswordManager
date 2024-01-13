from .connection import Connection


class Structure:

    def __init__(self, host: str, port: str, db_name: str, user: str, password: str):
        self._db_connection = Connection(host, port, db_name, user, password)
        self._db_connection.connect()
        self._connection = self._db_connection.connection

    def create_tables(self):
        with self._connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS users 
                    (
                        user_id SERIAL PRIMARY KEY,
                        user_name VARCHAR(25),
                        user_password VARCHAR(25)
                    );
                    
                   CREATE TABLE IF NOT EXISTS keys 
                    (
                        key_id SERIAL PRIMARY KEY,
                        user_id INTEGER,
                        encryption_key VARCHAR(44),
                        FOREIGN KEY (user_id) REFERENCES users (user_id)
                    );
                    
                   CREATE TABLE IF NOT EXISTS services 
                    (
                        service_id SERIAL PRIMARY KEY,
                        service_name TEXT
                    );
                    
                   CREATE TABLE IF NOT EXISTS passwords
                    (
                        password_id SERIAL PRIMARY KEY,
                        user_id INTEGER,
                        service_id INTEGER, 
                        login VARCHAR(50),
                        encrypted_password VARCHAR(255),
                        clue VARCHAR(25),
                        FOREIGN KEY (user_id) REFERENCES users (user_id),
                        FOREIGN KEY (service_id) REFERENCES services (service_id)
                    );"""
            )
            print('Successfully created table')
