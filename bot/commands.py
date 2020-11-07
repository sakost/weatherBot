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
