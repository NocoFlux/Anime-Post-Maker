# config.py
import os
import logging
from logging.handlers

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7848802187:AAHB57UFUFv0fRR_htevJhsmDT5hf-rfknE") # Get from @BotFather
APP_ID = int(os.environ.get("APP_ID", "26254064")) # Get from my.telegram.org
API_HASH = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c") # Get from my.telegram.org
OWNER_ID = int(os.environ.get("OWNER_ID", "5296584067")) # Your Telegram ID, get from @userinfobot
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002176591513")) # Channel ID (with -100 prefix)

# AniList API for anime data
ANILIST_API = "https://graphql.anilist.co"

# Example GraphQL query for recent anime
ANIME_QUERY = """
query {
  Page(page: 1, perPage: 10) {
    media(type: ANIME, sort: TRENDING_DESC) {
      id
      title {
        romaji
      }
      description
      coverImage {
        large
      }
    }
  }
}
"""

LOG_FILE_NAME = "tg-anime-news-bot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
