from cryptography.fernet import Fernet


class Encryption:

    @staticmethod
    def create_encryption_key() -> bytes:
        return Fernet.generate_key()

    @staticmethod
    def encode_password(key: bytes, password: str) -> bytes:
        cipher_suite = Fernet(key)
        encoded_password = cipher_suite.encrypt(password.encode())
        return encoded_password

    @staticmethod
    def decode_password(key: bytes, encrypted_password: bytes) -> str:
        cipher_suite = Fernet(key)
        decoded_password = cipher_suite.decrypt(encrypted_password)
        return decoded_password.decode()
