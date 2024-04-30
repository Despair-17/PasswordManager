# PasswordManager
Менеджер паролей, хранящий данные различных сервисов в базе данных (локальной или удаленной) в зашифрованном виде.

## Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Despair-17/PasswordManager.git
   ```
2. Создайте виртуальное окружение:
   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat на Windows
   source venv/bin/activate на Linux
   ```
3. Установите зависимости
   ```bash
   pip install -r requirements.txt
   ```
4. Впишите в файле database/config.py в класс ConnectionParameters параметры подключения к БД: 
   ```bash
   DB_HOST - хост БД
   DB_PORT - порт БД
   DB_USER - логин пользователя БД
   DB_PASS - пароль пользователя БД
   DB_NAME - название БД (создайте БД если её нет)
   ```
5. Запуск приложения из корневой папки:
   ```bash
   python main.py
   ```
