from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22175021"))
API_HASH = getenv("API_HASH", "9dd328229c3bb96dc1a112c3eac79a1a")

BOT_TOKEN = getenv("BOT_TOKEN", "7476307432:AAEktgA0zuJvyH02NzoPdbwhgoSTasgtaK0")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://avineyjr004:Team_HDSTR@cluster0.oxbmm.mongodb.net/retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", 655594746))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/filmy_tube")
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/7f02fa86d8b5f924be21b.jpg")
