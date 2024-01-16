from .user import User
from database import DatabaseService, ConnectionParameters
from exceptions import *


class Registration(User):

    def create_account(self) -> bool:
        try:
            with DatabaseService(*ConnectionParameters().fields) as cursor:
                cursor.add_user_data(self.login, self.password)
            return True
        except (LoginExistsError, InvalidLenLogin,
                InvalidSymbolsLogin, InvalidSymbolsLogin,
                InvalidLenPassword, InvalidPasswordComplexity):
            return False
