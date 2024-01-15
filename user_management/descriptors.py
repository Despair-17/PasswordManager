from abc import ABC, abstractmethod
import re
from exceptions import InvalidLenLogin, InvalidSymbolsLogin, InvalidLenPassword, InvalidPasswordComplexity


class AbstractDescriptor(ABC):
    _REGEX_LOGIN = re.compile(r'^\w+$')
    _REGEX_PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

    def __set_name__(self, owner, attr):
        self._attr = f'_{attr}'

    # Этот должен быть тоже абстрактным
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('invalid data type, str required')
        setattr(instance, self._attr, value.lower())

    @abstractmethod
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self._attr)

    @abstractmethod
    def _is_valid(self, value: str) -> bool:
        pass


class CorrectLogin(AbstractDescriptor):

    def __get__(self, instance, owner):
        instance_attr = getattr(instance, self._attr)
        if len(instance_attr) > 50:
            raise InvalidLenLogin('login too long')
        if len(instance_attr) < 4:
            raise InvalidLenLogin('login too short')
        if self._is_valid(instance_attr):
            raise InvalidSymbolsLogin(
                'the login can contain letters of the Latin alphabet (a–z), numbers (0–9) and periods (.)'
            )
        return super().__get__(instance, owner)

    def _is_valid(self, value: str) -> bool:
        return not bool(self.__class__._REGEX_LOGIN.match(value))


class CorrectPassword(AbstractDescriptor):

    def __get__(self, instance, owner):
        instance_attr = getattr(instance, self._attr)
        if len(instance_attr) > 50:
            raise InvalidLenPassword('password too long')
        if len(instance_attr) < 4:
            raise InvalidLenPassword('password too short')
        if self._is_valid(instance_attr):
            raise InvalidPasswordComplexity(
                'the password must contain at least one number, an uppercase and a lowercase letter'
            )
        return super().__get__(instance, owner)

    def _is_valid(self, value: str) -> bool:
        return not bool(self.__class__._REGEX_PASSWORD.match(value))
