from pyrogram import Client
from datetime import datetime
import logging

from config import API_HASH, APP_ID, LOGGER, BOT_TOKEN, CHANNEL_ID

import pyrogram.utils
pyrogram.utils.MIN_CHANNEL_ID = -1002176591513

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        try:
            await self.send_message(CHANNEL_ID, "⚡️ Bot is alive")
            self.LOGGER.info(f"✅ Bot has access to channel {CHANNEL_ID}")
        except Exception as e:
            self.LOGGER.error(f"❌ Bot lacks channel access: {str(e)}")
        
        self.LOGGER.info(f"Bot Started as {usr_bot_me.first_name}")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot Stopped!")
      
