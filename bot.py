import telebot
import json
from db_connection import DB

with open("config.json", 'r') as f:
    config = json.load(f)
with open("commands.json", 'r') as f:
    commands = json.load(f)

bot = telebot.TeleBot(config['token'])
base = DB(config["url"], config["port"], config["login"], config["password"],
          config["name"])
for command in commands:
    base.create_query(command, commands[command])


def check_user_id(function):
    def wrapper(message):
        if message.chat.id != config['user_id']:
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
def commands(message):
    command = ' '.join(message.text.split(' ')[:2])
    if len(message.text.split(' ')) > 2:
        args = message.text.split(' ')[2:]

    if command in commands:
        res = base.use_query(command, args)
        bot.send_message(message.chat.id, str(res))
    else:
        bot.send_message(message.chat.id, 'Не прописана комманда в файле '
                                          'commands.json')


if __name__ == '__main__':
    bot.polling()