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
        self.conn_parameters = ConnectionParameters().fields

    def create_account(self) -> None:
        try:
            with DatabaseService(*self.conn_parameters) as service:
                service.add_user_data(self.login, self.password)
        except LoginExistsError as err:
            print(err)
        except InvalidLenLogin as err:
            print(err)
        except InvalidSymbolsLogin as err:
            print(err)
        except InvalidLenPassword as err:
            print(err)
        except InvalidPasswordComplexity as err:
            print(err)
