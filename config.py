from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 655594746))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/filmy_tube")
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/7f02fa86d8b5f924be21b.jpg")
