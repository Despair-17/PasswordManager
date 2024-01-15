import bcrypt


class Hashing:

    @staticmethod
    def get_salt() -> bytes:
        return bcrypt.gensalt()

    @staticmethod
    def hash_password(password: str, salt: bytes) -> bytes:
        return bcrypt.hashpw(password.encode(), salt)

    @staticmethod
    def verify_password(input_password: str, hashed_password: str, stored_salt: str) -> bool:
        return bcrypt.hashpw(input_password.encode(), stored_salt.encode()) == hashed_password.encode()
