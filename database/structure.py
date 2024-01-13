from .connection import Connection


class Structure(Connection):

    def __init__(self, host: str, port: str, db_name: str, user: str, password: str):
        super().__init__(host, port, db_name, user, password)

    def create_tables(self):
        with self._connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS users 
                    (
                        user_id SERIAL PRIMARY KEY,
                        user_name VARCHAR(50) UNIQUE NOT NULL,
                        user_password VARCHAR(50) NOT NULL
                    );
                    
                   CREATE TABLE IF NOT EXISTS keys 
                    (
                        key_id SERIAL PRIMARY KEY,
                        user_id INTEGER,
                        encryption_key VARCHAR(44),
                        FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
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
                        clue VARCHAR(30),
                        FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
                        FOREIGN KEY (service_id) REFERENCES services (service_id)
                    );"""
            )
        print('Successfully created table')
