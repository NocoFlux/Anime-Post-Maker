from telegram import Update
from telegram.ext import CallbackContext
import config

def is_admin(update: Update) -> bool:
    if update.effective_user.id == int(config.TG_OWNER_ID):
        return True
    else:
        update.message.reply_text("You are not authorized to use this command.")
        return False
