from .connection import Connection, LoginExistsError
from psycopg2 import errors


class UserService(Connection):

    def __init__(self, host: str, port: str, db_name: str, user: str, password: str):
        super().__init__(host, port, db_name, user, password)

    def add_user_data(self, username: str, hashed_password: str, salt: str, encryption_key: str) -> None:
        with self._connection.cursor() as cursor:
            try:
                cursor.execute(
                    f"""INSERT INTO users (username, hashed_password, salt) 
                        values ('{username}', '{hashed_password}', '{salt}');
                        
                        INSERT INTO keys (user_id, encryption_key)
                        values (
                            (SELECT user_id FROM users WHERE username = '{username}'), 
                            '{encryption_key}'
                        );"""
                )
            except errors.UniqueViolation as err:
                raise LoginExistsError(f'User name {username} is busy!') from err

    def get_user_data(self, username: str) -> tuple[int, str, str]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT user_id, hashed_password, salt
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
