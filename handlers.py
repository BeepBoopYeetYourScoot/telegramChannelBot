import loguru
from telegram import Update
from telegram.ext import ContextTypes

from conf import BOT_USERNAME


def handle_user_text(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Henlo there"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    loguru.logger.info(
        f"User ({update.message.chat.id}) in {message_type}: " f"{text}"
    )

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, "").strip()
            response = handle_user_text(new_text)
        else:
            return
    else:
        response = handle_user_text(text)
    loguru.logger.info(response)
    await update.message.reply_text(response)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loguru.logger.info(f"{update=} caused {context.error=}")
