from database import DatabaseService, ConnectionParameters
from exceptions import LoginExistsError, InvalidLenLogin, InvalidSymbolsLogin
from exceptions import InvalidLenPassword, InvalidPasswordComplexity
from .descriptors import CorrectLogin, CorrectPassword


class Registration:
    login = CorrectLogin()
    password = CorrectPassword()

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def create_account(self) -> None:
        try:
            with DatabaseService(*ConnectionParameters().fields) as service:
                service.add_user_data(self.login, self.password)
        except (LoginExistsError, InvalidLenLogin,
                InvalidSymbolsLogin, InvalidSymbolsLogin,
                InvalidLenPassword, InvalidPasswordComplexity) as err:
            print(err)
