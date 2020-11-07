from telebot import TeleBot
from telebot.types import BotCommand

from .config import SETTINGS

bot = TeleBot(SETTINGS['TOKEN'])

commands_list = {}


def initialize_bot(bot: TeleBot):
    bot_commands = []
    for handler in bot.message_handlers:
        commands = tuple(handler['filters']['commands'])
        if commands:
            func = handler['function']
            desc = commands_list[commands] = func.__doc__
            desc = desc if desc else ''

            if len(desc) > 3:
                for cmd in commands:
                    bot_commands.append(BotCommand(cmd, desc))
    bot.set_my_commands(bot_commands)

