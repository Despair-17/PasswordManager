from .connection import Connection
from security import Encryption


class DatabaseService:

    def __init__(self, host: str, port: str, db_name: str, user: str, password: str):
        self._db_connection = Connection(host, port, db_name, user, password)
        self._db_connection.connect()
        self._connection = self._db_connection.connection
        self._connection.autocommit = True

    def add_user_data(self, login: str, password: str) -> None:
        # Потенциальная ошибка, при добавлении уже существующих логинов
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO users (user_name, user_password) 
                    values ('{login}', '{password}');
                    
                    INSERT INTO keys (user_id, encryption_key)
                    values (
                        (SELECT user_id FROM users WHERE user_name = '{login}'), 
                        '{Encryption.create_encryption_key().decode()}'
                    )"""
            )

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

    def disconnect(self) -> None:
        self._db_connection.disconnect()
