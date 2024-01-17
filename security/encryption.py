from cryptography.fernet import Fernet


class Encryption:

    @staticmethod
    def create_encryption_key() -> str:
        return Fernet.generate_key().decode()

    @staticmethod
    def encode_password(key: str, password: str) -> str:
        cipher_suite = Fernet(key.encode())
        encoded_password = cipher_suite.encrypt(password.encode())
        return encoded_password.decode()

    @staticmethod
    def decode_password(key: str, encrypted_password: str) -> str:
        cipher_suite = Fernet(key.encode())
        decoded_password = cipher_suite.decrypt(encrypted_password.encode())
        return decoded_password.decode()
