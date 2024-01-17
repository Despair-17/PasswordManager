from database import PasswordService
from database import ConnectionParameters


class PasswordManager(PasswordService):

    def __init__(self):
        super().__init__(*ConnectionParameters().fields)

    def add_password(self, user_id: int, service_name: str, login: str, password: str, description: str = ''):
        super().add_password(user_id, service_name, login, password, description)

    def delete_password(self):
        pass

    def update_password(self):
        pass

    def get_passwords(self):
        pass
