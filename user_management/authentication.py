from .user import User
from database import UserService, ConnectionParameters
from security import Hashing


class Authentication(User):

    def __init__(self, login: str, password: str):
        super().__init__(login, password)
        self._hashed_password = None
        self._stored_salt = None

    def authenticate_account(self) -> bool:
        with UserService(*ConnectionParameters().fields) as cursor:
            user_data = cursor.get_user_data(getattr(self, '_login'))
            if not user_data:
                return False
            self._hashed_password, self._stored_salt = cursor.get_user_data(self.login)
            return Hashing.verify_password(getattr(self, '_password'), self._hashed_password, self._stored_salt)
