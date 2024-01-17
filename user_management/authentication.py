from .user import User
from database import UserService, ConnectionParameters
from security import Hashing


class Authentication(User):

    def __init__(self, login: str, password: str):
        super().__init__(login, password)
        self._hashed_password = None
        self._stored_salt = None

    def authenticate_account(self) -> tuple[int | None, bool]:
        with UserService(*ConnectionParameters().fields) as cursor:
            user_data = cursor.get_user_data(getattr(self, '_login'))
            if not user_data:
                return None, False
            user_id, self._hashed_password, self._stored_salt = user_data
            return user_id, Hashing.verify_password(getattr(self, '_password'),
                                                    self._hashed_password,
                                                    self._stored_salt)
