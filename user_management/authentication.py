from database import DatabaseService, ConnectionParameters
from exceptions import LoginExistsError, InvalidLenLogin, InvalidSymbolsLogin
from exceptions import InvalidLenPassword, InvalidPasswordComplexity
from .descriptors import CorrectLogin, CorrectPassword


class Authentication:
    login = CorrectLogin()
    password = CorrectPassword()

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
