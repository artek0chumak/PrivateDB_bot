import telebot
import json
from db_connection import Postgres, Sqlite3
from collections import Iterable

with open("config.json", 'r') as f:
    config_bot = json.load(f)["bot"]
    config_server = json.load(f)["server"]
with open("commands.json", 'r') as f:
    commands = json.load(f)

bot = telebot.TeleBot(config_bot['token'])
if config_server["type"] == 'postgresql':
    base = Postgres(config_server["url"], config_server["port"], config_server["login"],
              config_server["password"], config_server["name"])
elif config_bot["type"] == 'sqlite3':
    base = Sqlite3(config_server["filepath"], config_server["name"])
for command in commands:
    base.create_query(command, commands[command])


def check_user_id(function):
    def wrapper(message):
        if message.chat.id != config_bot['user_id']:
            bot.send_message(message.chat.id, 'Вы не можете использовать бота!')
        else:
            function(message)

    return wrapper


@bot.message_handler(commands=['start'])
@check_user_id
def start(message):
    bot.send_message(message.chat.id, 'Приветствую!')


@bot.message_handler(content_types=['text'])
@check_user_id
def command_use(message):
    command = ' '.join(message.text.lower().split(' ')[:2])
    if len(message.text.split(' ')) > 2:
        args = message.text.lower().split(' ')[2:]
    else:
        args = []

    if command in commands:
        res = base.use_query(command, *args)
        if all(isinstance(i, Iterable) for i in res):
            bot.send_message(message.chat.id,
                             "\n".join(' '.join(col) for col in res))
        else:
            bot.send_message(message.chat.id, ' '.join(map(str,res)))
    else:
        bot.send_message(message.chat.id, 'Не прописана комманда в файле '
                                          'commands.json')


if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=120)