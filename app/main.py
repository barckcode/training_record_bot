import os
from telegram.ext import Updater

# Internal Modules
from commands.start import start_command


updater = Updater(
    token=os.environ['TOKEN_BOT'],
    use_context=True
)


dispatcher = updater.dispatcher


# Commands List
dispatcher.add_handler(start_command)


if __name__ == '__main__':
    updater.start_polling()
