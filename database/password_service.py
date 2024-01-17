from .connection import Connection
from typing import Iterator


class PasswordService(Connection):

    def __init__(self, host: str, port: str, db_name: str, user: str, password: str):
        super().__init__(host, port, db_name, user, password)

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

    def get_encryption_key(self, user_id: int) -> str:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT encryption_key
                    FROM keys
                    WHERE user_id = '{user_id}'"""
            )
            return cursor.fetchone()[0]

    def add_password(self, user_id: int, service_id: int, login: str,
                     encrypted_password: str, description: str) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO passwords (user_id, service_id, login, encrypted_password, description)
                    VALUES ('{user_id}', '{service_id}', '{login}', '{encrypted_password}', '{description}');"""
            )

    def get_passwords(self, user_id: int) -> Iterator[tuple[str, str, str, str]]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT service_name, login, encrypted_password, description
                    FROM passwords as t1 inner join services as t2 on t1.service_id = t2.service_id
                    WHERE user_id = '{user_id}'
                    ORDER BY service_name, login;"""
            )
            yield from cursor.fetchall()

    def update_password(self, user_id: int, service_id: int, login: str, new_encrypted_password: str) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""UPDATE passwords
                    SET encrypted_password = '{new_encrypted_password}'
                    WHERE user_id = '{user_id}' and service_id = '{service_id}' and login = '{login}'; """
            )

    def delete_password(self, user_id: int, service_id: int, login: str) -> None:
        with self._connection.cursor() as cursor:
            cursor.execute(
                f"""DELETE
                    FROM passwords
                    WHERE user_id = '{user_id}' and service_id = '{service_id}' and login = '{login}';"""
            )
