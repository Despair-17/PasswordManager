from .connection import Connection, LoginExistsError
from security import Encryption
from psycopg2 import errors
from security import Hashing


class DatabaseService(Connection):

    def __init__(self, host: str, port: str, db_name: str, user: str, password: str):
        super().__init__(host, port, db_name, user, password)

    def add_user_data(self, username: str, password: str) -> None:
        with self._connection.cursor() as cursor:
            salt = Hashing.get_salt()
            hashed_password = Hashing.hash_password(password, salt)
            try:
                cursor.execute(
                    f"""INSERT INTO users (username, hashed_password, salt) 
                        values ('{username}', '{hashed_password.decode()}', '{salt.decode()}');
                        
                        INSERT INTO keys (user_id, encryption_key)
                        values (
                            (SELECT user_id FROM users WHERE username = '{username}'), 
                            '{Encryption.create_encryption_key()}'
                        );"""
                )
            except errors.UniqueViolation as err:
                raise LoginExistsError(f'User name {username} is busy!') from err

    def get_user_data(self, username: str) -> tuple:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT hashed_password, salt
                    FROM users
                    WHERE username = '{username}';"""
            )
            user_data = cursor.fetchone()
            return user_data

    def del_user_data(self, username: str) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""DELETE
                    FROM users
                    WHERE user_name = '{username}';"""
            )

    def get_or_insert_service_id(self, service_name: str) -> int:
        service_name = service_name.lower()
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO services (service_id, service_name)
                    VALUES (DEFAULT, '{service_name}')
                    ON CONFLICT (service_name) DO NOTHING;
                    
                    SELECT service_id
                    FROM services
                    WHERE service_name = '{service_name}';"""
            )
            return cursor.fetchone()[0]

    def insert_password(self, user_id: int, service_id: int, login: str, password: str, description: str = '') -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT encryption_key
                    FROM keys
                    WHERE user_id = '{user_id}'"""
            )
            encryption_key = cursor.fetchone()[0]
            encrypted_password = Encryption.encode_password(encryption_key, password)

            cursor.execute(
                f"""INSERT INTO passwords (user_id, service_id, login, encrypted_password, description)
                    VALUES ('{user_id}', '{service_id}', '{login}', '{encrypted_password}', '{description}');"""
            )
