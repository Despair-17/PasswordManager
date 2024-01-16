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
                        username VARCHAR(50) UNIQUE NOT NULL,
                        hashed_password VARCHAR(60) NOT NULL,
                        salt VARCHAR(29) NOT NULL
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
                        service_name TEXT UNIQUE NOT NULL
                    );
                    
                   CREATE TABLE IF NOT EXISTS passwords
                    (
                        password_id SERIAL PRIMARY KEY,
                        user_id INTEGER,
                        service_id INTEGER, 
                        login VARCHAR(50),
                        encrypted_password VARCHAR(255),
                        description VARCHAR(30),
                        FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
                        FOREIGN KEY (service_id) REFERENCES services (service_id)
                    );"""
            )
        print('Successfully created tables')

    def delete_table(self):
        with self._connection.cursor() as cursor:
            cursor.execute(
                """DROP TABLE passwords;
                   DROP TABLE keys;
                   DROP TABLE users;
                   DROP TABLE services;"""
            )
        print('Successfully droped tables')