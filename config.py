# config.py
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # Get from @BotFather
APP_ID = int(os.environ.get("APP_ID", "")) # Get from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") # Get from my.telegram.org
OWNER_ID = int(os.environ.get("OWNER_ID", "")) # Your Telegram ID, get from @userinfobot
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) # Channel ID (with -100 prefix)

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
