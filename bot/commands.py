import requests
from telebot.types import Message

from .bot import bot, commands_list

hi_message_translations = {
    'en': 'Hi!\nTo get a list of commands send /help',
    'ru': 'Привет!\nЧтобы получить список команд отправь /help',
}

commands_list_translations = {
    'en': 'List of commands:\n',
    'ru': 'Список команд:\n',
}

default_lang = 'en'


@bot.message_handler(['start'])
def _(message: Message):
    """greeting message"""
    lang = message.from_user.language_code
    bot.reply_to(message, hi_message_translations.get(lang, hi_message_translations[default_lang]))


@bot.message_handler(['help'])
def _(message: Message):
    """list all commands"""
    lang = message.from_user.language_code
    text = commands_list_translations.get(lang, commands_list_translations[default_lang])

    for commands, description in commands_list.items():
        text += ', '.join(map(lambda x: '/' + x, commands))
        if description:
            text += ' - ' + description
        text += '\n'

    bot.reply_to(message, text)


@bot.message_handler(['weather'])
def _(message: Message):
    """weather forecast"""
    command = message.text.split()[0]
    text = message.text[len(command):].strip()
    city = text
    if not city:
        bot.reply_to(message, 'command /weather needs an argument - city\nfor example: `/weather Moscow`',
                     parse_mode='MARKDOWN')
    else:
        req = requests.get(f'https://wttr.in/{city}?0?q?T')
        bot.reply_to(message, f'```{req.text}```', parse_mode='MARKDOWN')

