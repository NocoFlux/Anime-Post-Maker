from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Post Maker Bot! Use /create to start creating a post.')
