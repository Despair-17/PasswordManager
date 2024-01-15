from .descriptors import CorrectLogin, CorrectPassword


class User:
    login = CorrectLogin()
    password = CorrectPassword()

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
