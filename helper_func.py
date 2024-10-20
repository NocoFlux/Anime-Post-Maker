# helper_func.py
from datetime import datetime
from config import OWNER_ID

def check_owner(func):
    async def wrapper(client, message):
        if message.from_user.id != OWNER_ID:
            await message.reply("⛔️ Only owner can use this command")
            return
        await func(client, message)
    return wrapper

def get_readable_time(seconds: int) -> str:
    result = ''
    (days, remainder) = divmod(int(seconds), 86400)
    days = f'{days}d:' if days != 0 else ''
    (hours, remainder) = divmod(remainder, 3600)
    hours = f'{hours}h:' if hours != 0 else ''
    (minutes, seconds) = divmod(remainder, 60)
    minutes = f'{minutes}m:' if minutes != 0 else ''
    seconds = f'{seconds}s'
    result = f"{days}{hours}{minutes}{seconds}"
    return result
