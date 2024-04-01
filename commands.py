from telegram import Update
from telegram.ext import ContextTypes

START_COMMAND_TEXT = "Hello and welcome!"
HELP_COMMAND_TEXT = (
    "I am alone_in_bkk channel bot.Please ensure you're subscribed!"
)
ECHO_COMMAND_TEXT = "Custom command echoes slowly...!"
CHANNEL_INFO_TEXT = (
    "Channel my thought to Collective to spread quality "
    "content all around the globe"
)
USEFUL_LINKS_COMMAND = """
https://t.me/makeyouswag
https://t.me/alone_in_bkk
https://hh.ru/applicant/resumes/view?resume=ee745cc9ff08b259150039ed1f30304d586b32
https://github.com/BeepBoopYeetYourScoot?tab=repositories
https://www.linkedin.com/in/dmitrii-zavorotnii-a8a71b150/
"""


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_COMMAND_TEXT)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_COMMAND_TEXT)


async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ECHO_COMMAND_TEXT)


async def channel_info_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(CHANNEL_INFO_TEXT)


async def links_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(USEFUL_LINKS_COMMAND)
