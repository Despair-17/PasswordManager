from database import PasswordService
from database import ConnectionParameters
from security import Encryption
from itertools import starmap, chain
from typing import Iterator


class PasswordManager(PasswordService):

    def __init__(self):
        super().__init__(*ConnectionParameters().fields)

    def add_password(self, user_id: int, service_name: str, login: str, password: str, description: str = '') -> None:
        service_id = super().get_or_insert_service_id(service_name)
        encryption_key = super().get_encryption_key(user_id)
        encrypted_password = Encryption.encode_password(encryption_key, password)
        super().add_password(user_id, service_id, login, encrypted_password, description)

    def get_passwords(self, user_id: int) -> Iterator[tuple[str, str, str, str]]:
        iterator_passwords = super().get_passwords(user_id)
        encryption_key = super().get_encryption_key(user_id)
        iterator_passwords = starmap(lambda service, login, password, description:
                                     (
                                         service,
                                         login,
                                         Encryption.decode_password(encryption_key, password),
                                         description
                                     ),
                                     iterator_passwords)
        iterator_titles = (('Services', 'Logins', 'Passwords', 'Descriptions'),)
        iterator_passwords = chain(iterator_titles, iterator_passwords)
        return iterator_passwords

    def update_password(self, user_id: int, service_name: str, login: str, new_password: str) -> None:
        service_id = super().get_or_insert_service_id(service_name)
        encryption_key = super().get_encryption_key(user_id)
        super().update_password(user_id, service_id, login, Encryption.encode_password(encryption_key, new_password))

    def delete_password(self, user_id: int, service_name: str, login: str):
        service_id = super().get_or_insert_service_id(service_name)
        super().delete_password(user_id, service_id, login)

    @staticmethod
    def gen_password():
        pass
