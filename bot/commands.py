from telebot.types import Message

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


@bot.message_handler(['start', 'help'])
def _(message: Message):
    lang = message.from_user.language_code
    bot.reply_to(message, hi_messages.get(lang, hi_messages[default_lang]))

