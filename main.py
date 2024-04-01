import loguru
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from commands import (
    start_command,
    help_command,
    echo_command,
    channel_info_command,
    links_command,
)
from conf import TOKEN
from handlers import handle_message, error_handler

COMMAND_HANDLER_MAP = {
    "start": start_command,
    "help": help_command,
    "echo": echo_command,
    "info": channel_info_command,
    "links": links_command,
}


if __name__ == "__main__":
    loguru.logger.info("Starting bot")
    app = Application.builder().token(TOKEN).build()

    # Commands
    for command_name, callback in COMMAND_HANDLER_MAP.items():
        app.add_handler(CommandHandler(command_name, callback))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error_handler)

    loguru.logger.info("Polling")
    app.run_polling(poll_interval=3)
