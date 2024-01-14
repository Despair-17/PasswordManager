from dataclasses import dataclass


@dataclass
class ConnectionParameters:
    host: str = 'localhost'
    port: str = '5432'
    db_name: str = 'PasswordManager'
    user: str = 'postgres'
    password: str = '0601'

    def __post_init__(self):
        self.fields = self.host, self.port, self.db_name, self.user, self.password
