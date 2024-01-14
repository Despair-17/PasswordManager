from database import DatabaseService
from database import ConnectionParameters
from exceptions import LoginExistsError


class Registration:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.conn_parameters = ConnectionParameters().fields

    def create_account(self):
        try:
            with DatabaseService(*self.conn_parameters) as service:
                service.add_user_data(self.login, self.password)
        except LoginExistsError as err:
            print(err)
