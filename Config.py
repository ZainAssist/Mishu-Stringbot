from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","21989865"))
API_HASH = getenv("API_HASH","90e5e665feb30e647bef49884cc006u15")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID","6048907378"))

MONGO_DB_URI = getenv("mongodb+srv://zainu:1234567890@cluster0.c12d3ih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN","About_Zain")
