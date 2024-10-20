from pyrogram import Client
from aiohttp import web
import asyncio
from config import BOT_TOKEN, APP_ID, API_HASH, LOGGER

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="AnimeNewsBot",
            api_id=APP_ID,
            api_hash=API_HASH,
            plugins=dict(root="plugins"),
            workers=200,
            bot_token=BOT_TOKEN
        )
        self.web_app = web.Application()
        self.web_app.router.add_get("/", self.health_check)

    async def health_check(self, request):
        return web.Response(text="Bot is running!")

    async def start_web_server(self):
        runner = web.AppRunner(self.web_app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', 8000)
        await site.start()
        LOGGER.info("Web server started on port 8000")

    def run(self):
        async def start_bot():
            await self.start()
            LOGGER.info("✅ Bot Started Successfully!")
            await self.start_web_server()
            await self.idle()

        asyncio.get_event_loop().run_until_complete(start_bot())
