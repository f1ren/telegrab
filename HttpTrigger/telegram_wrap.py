#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import io
import json
import logging
import os
import re

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Dispatcher, MessageHandler, Filters

from HttpTrigger.web_browser import get_screenshot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', 'empty_token')

SINGLETONS = {}


def log_event(*args):
    update = get_telegram_args(args)

    keyboard = [
        [
            InlineKeyboardButton(text, callback_data=text)
            for text in ("🌙 Sleep", "🌞 Wake")
        ],
        [
            InlineKeyboardButton(text, callback_data=text)
            for text in ("🍼 Bottle", "🍔 food")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(*args):
    update = get_telegram_args(args)
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=query.data)


def help_command(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def echo(*args):
    """Echo the user message."""
    update = get_telegram_args(args)
    text = update.message.text
    URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    urls = [r[0] for r in re.findall(URL_REGEX, text)]
    if urls:
        update.message.reply_text('\n'.join(urls))
        for url in urls:
            update.message.reply_photo(photo=io.BytesIO(get_screenshot(url)))


def get_telegram_args(args):
    update = [arg for arg in args if type(arg) is Update][0]
    return update


def add_handlers_to_dispatcher(updater):
    updater.dispatcher.add_handler(CommandHandler('log', log_event))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))


def polling_main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    bot = Bot(TELEGRAM_TOKEN)
    updater = Updater(bot=bot, use_context=True)
    add_handlers_to_dispatcher(updater)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


def web_handler(body: dict):
    dispatcher = get_sync_dispatcher()
    update = Update.de_json(body, dispatcher.bot)
    updater = Updater(dispatcher=dispatcher, workers=None)
    add_handlers_to_dispatcher(updater)
    updater.dispatcher.process_update(update)


def get_sync_dispatcher():
    if 'dispatcher' not in SINGLETONS:
        SINGLETONS['dispatcher'] = init_sync_dispatcher()
    return SINGLETONS['dispatcher']


def init_sync_dispatcher():
    logging.info(f'TELEGRAM_TOKEN = {TELEGRAM_TOKEN[:3]}')
    bot = Bot(TELEGRAM_TOKEN)
    # Synchronous: No queue, no workers
    dispatcher = Dispatcher(bot, update_queue=None, workers=0)
    return dispatcher


if __name__ == '__main__':
    polling_main()
