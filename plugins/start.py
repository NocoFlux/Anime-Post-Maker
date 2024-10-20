from pyrogram import Client, filters
from helper_func import get_readable_time
from datetime import datetime

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    uptime = get_readable_time((datetime.now() - client.uptime).total_seconds())
    await message.reply(f"Bot is alive!\nUptime: {uptime}")

@Client.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    start = datetime.now()
    reply = await message.reply("Pinging...")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await reply.edit(f"Pong!\nResponse Time: `{ms}ms`")
