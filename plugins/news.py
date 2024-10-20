from pyrogram import Client, filters
from helper_func import check_owner
import aiohttp
import asyncio
from config import *

news_task = None

@Client.on_message(filters.command("startnews") & filters.user(OWNER_ID))
@check_owner
async def start_news_cmd(client, message):
    global news_task
    if news_task:
        await message.reply("News service already running!")
        return
    
    news_task = asyncio.create_task(news_monitor(client))
    await message.reply("ðŸŸ¢ Started anime news service")

@Client.on_message(filters.command("stopnews") & filters.user(OWNER_ID))
@check_owner
async def stop_news_cmd(client, message):
    global news_task
    if news_task:
        news_task.cancel()
        news_task = None
        await message.reply("ðŸ”´ Stopped anime news service")
    else:
        await message.reply("News service not running!")

async def news_monitor(client):
    last_id = None
    while True:
        try:
            # Replace with your preferred anime news API
            async with aiohttp.ClientSession() as session:
                async with session.get("YOUR_ANIME_API_ENDPOINT") as response:
                    if response.status == 200:
                        news = await response.json()
                        if news['id'] != last_id:
                            last_id = news['id']
                            caption = f"ðŸŒŸ {news['title']}\n\n{news['description']}"
                            await client.send_photo(
                                CHANNEL_ID,
                                news['image'],
                                caption=caption
                            )
            await asyncio.sleep(300)
        except Exception as e:
            LOGGER.error(f"Error in news monitor: {e}")
            await asyncio.sleep(60)
