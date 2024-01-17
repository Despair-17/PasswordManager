from .connection import Connection
from security import Encryption


class PasswordService(Connection):

    def __init__(self, host: str, port: str, db_name: str, user: str, password: str):
        super().__init__(host, port, db_name, user, password)

    def _get_or_insert_service_id(self, service_name: str) -> int:
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

    def add_password(self, user_id: int, service_name: str, login: str, password: str, description: str) -> None:
        service_id = self._get_or_insert_service_id(service_name)

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
