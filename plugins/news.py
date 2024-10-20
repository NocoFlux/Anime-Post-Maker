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
    await message.reply("🟢 Started anime news service")

@Client.on_message(filters.command("stopnews") & filters.user(OWNER_ID))
@check_owner
async def stop_news_cmd(client, message):
    global news_task
    if news_task:
        news_task.cancel()
        news_task = None
        await message.reply("🔴 Stopped anime news service")
    else:
        await message.reply("News service not running!")

async def news_monitor(client):
    last_id = None
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                # Proper POST request to AniList GraphQL API
                async with session.post(
                    ANILIST_API,
                    json={'query': ANIME_QUERY}
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        anime = data['data']['Page']['media'][0]
                        
                        if anime['id'] != last_id:
                            last_id = anime['id']
                            title = anime['title']['english'] or anime['title']['romaji']
                            desc = anime['description']
                            if desc and len(desc) > 800:
                                desc = desc[:800] + "..."
                            
                            caption = f"🌟 {title}\n\n{desc}"
                            
                            await client.send_photo(
                                chat_id=CHANNEL_ID,
                                photo=anime['coverImage']['extraLarge'],
                                caption=caption
                            )
                            LOGGER.info(f"Posted new anime: {title}")
            
            await asyncio.sleep(300)  # Check every 5 minutes
        except Exception as e:
            LOGGER.error(f"Error in news monitor: {e}")
            await asyncio.sleep(60)