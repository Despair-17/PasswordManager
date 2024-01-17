from .user import User
from database import UserService, ConnectionParameters
from exceptions import *


class Registration(User):

    def create_account(self) -> bool:
        try:
            with UserService(*ConnectionParameters().fields) as cursor:
                cursor.add_user_data(self.login, self.password)
                print('Successfully created account')
            return True
        except (LoginExistsError, InvalidLenLogin,
                InvalidSymbolsLogin, InvalidSymbolsLogin,
                InvalidLenPassword, InvalidPasswordComplexity):
            return False
