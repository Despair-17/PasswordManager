from .user import User
from database import UserService, ConnectionParameters
from security import Encryption, Hashing
from exceptions import *


class Registration(User):

    def create_account(self) -> bool:
        try:
            with UserService(*ConnectionParameters().fields) as cursor:
                salt = Hashing.get_salt()
                hashed_password = Hashing.hash_password(self.password, salt)
                encryption_key = Encryption.create_encryption_key()
                cursor.add_user_data(self.login, hashed_password.decode(), salt.decode(), encryption_key)
                print('Successfully created account')
            return True
        except (LoginExistsError, InvalidLenLogin,
                InvalidSymbolsLogin, InvalidSymbolsLogin,
                InvalidLenPassword, InvalidPasswordComplexity):
            return False
