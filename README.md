# PrivateDB_bot
Простой бот для работы с базой данных PostreSQL. Возможна работа только с одним пользователем. Настраивается в config.json. Команды для работы с базой данных находятся в файле commands.json.

## Используемые библиотеки
- [python 3.6](https://www.python.org/)
    - [telebot](https://github.com/eternnoir/pyTelegramBotAPI)
    - [py-postgresql](https://pypi.org/project/py-postgresql/)
    - [pandas](https://pandas.pydata.org/)

## Запуск
Вместе с файлом bot.py должен находится файл config.json и  commands.json
```
python bot.py
```

#### Пример config.json
```json
{
  "token": "your_bot_token",
  "user_id": "123456789",
  "url": "url_to_db",
  "port": "1234",
  "login": "login",
  "password": "password",
  "name": "db_name"
}
```

#### Пример commands.json
```json
{
  "command_name": "select * from table where = {0}",
  "insert": "insert into table values (30, {0})",
  "show": "select * from table"
}
```
Аргументы к командам пишутся в формате [python string](https://docs.python.org/2/library/string.html)

## Пример использования бота
```
show

example 100

show
```