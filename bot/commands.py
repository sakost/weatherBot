from telebot.types import Message, User

from .bot import bot

hi_messages = {
    'en': 'Hi!\nTo get a list of commands send /help',
    'ru': 'Привет!\nЧтобы получить список команд отправь /help',
}

commands_list = {
    'en': 'List of commands:\n',
    'ru': 'Список команд:\n',
}

default_lang = 'en'


@bot.message_handler(['start'])
def _(message: Message):
    lang = message.from_user.language_code
    bot.reply_to(message, hi_messages.get(lang, hi_messages[default_lang]))


@bot.message_handler(['help'])
def _(message: Message):
    lang = message.from_user.language_code
    text = commands_list.get(lang, commands_list[default_lang])

    for handler in bot.message_handlers:
        if handler['filters']['commands']:
            func = handler['function']
            func_doc = ' - ' + func.__doc__ if func.__doc__ else ''
            text += '\t' + ', '.join(handler['filters']['commands']) + func_doc + '\n'

    bot.reply_to(message, text)
