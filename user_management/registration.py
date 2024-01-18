from .user import User
from database import UserService, ConnectionParameters
from security import Encryption, Hashing
from exceptions import *


class Registration(User):

    def __init__(self, login: str, password: str):
        super().__init__(login, password)

    def create_account(self) -> str:
        try:
            with UserService(*ConnectionParameters().fields) as cursor:
                salt = Hashing.get_salt()
                login, password = self.login, self.password
                hashed_password = Hashing.hash_password(password, salt)
                encryption_key = Encryption.create_encryption_key()
                cursor.add_user_data(login, hashed_password.decode(), salt.decode(), encryption_key)
            return 'Successfully created account'
        except (LoginExistsError, InvalidLenLogin,
                InvalidSymbolsLogin, InvalidSymbolsLogin,
                InvalidLenPassword, InvalidPasswordComplexity) as err:
            return err.args[0]
