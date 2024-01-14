from .connection import Connection, LoginExistsError
from security import Encryption
from psycopg2 import errors


class DatabaseService(Connection):

    def __init__(self, host: str, port: str, db_name: str, user: str, password: str):
        super().__init__(host, port, db_name, user, password)

    def add_user_data(self, login: str, password: str) -> None:
        with self._connection.cursor() as cursor:
            try:
                cursor.execute(
                    f"""INSERT INTO users (user_name, user_password) 
                        values ('{login}', '{password}');
                        
                        INSERT INTO keys (user_id, encryption_key)
                        values (
                            (SELECT user_id FROM users WHERE user_name = '{login}'), 
                            '{Encryption.create_encryption_key().decode()}'
                        );"""
                )
            except errors.UniqueViolation as err:
                raise LoginExistsError(f'User name {login} is busy!') from err

    def get_user_data(self, login: str) -> tuple:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT *
                    FROM users
                    WHERE user_name = '{login}';"""
            )
            return cursor.fetchone()

    def del_user_data(self, login: str) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""DELETE
                    FROM users
                    WHERE user_name = '{login}';"""
            )
