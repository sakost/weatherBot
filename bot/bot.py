from telebot import TeleBot

from .config import SETTINGS

bot = TeleBot(SETTINGS['TOKEN'])


def initialize_bot(bot):
    pass
