from .connection import Connection, LoginExistsError
from security import Encryption, Hashing
from psycopg2 import errors


class UserService(Connection):

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
