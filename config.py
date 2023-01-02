import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "15954332")
    API_HASH = getenv("API_HASH", "85adea6f1eaf068b707703b4846a9ced")
    TOKEN = getenv("TOKEN", "5970750070:AAGYVKWTOX5pecOIhhz6ghs4sdoSsyssS6c")
    OWNER_ID = getenv("OWNER_ID", "5134595693")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "5134595693")
    STRING_SESSION = getenv("STRING_SESSION", "1ApWapzMBu4UovB77DbJ7e3WhZATE7y8QHY540J1uGdX0ROgUsV0f6IiormYSkMtojl0bc4maHRF4cBNiZ6OwY6XaoJt_I6m-027yr4AtDkm_vogRXkaVy02YejV18vkuVcVlb1DbtwjJ42EnZySSeHaaCwuGZ8yQGTloCXkgb2T2G5--p8lXsqPFhmS8j-bkoY9jEDD56Uqjfs6cT9nTcdxPkvU3w7CkIvf9hYbVvt3ZIIC39qWDB-ql8swE33U7XyWSYEzqpEk62zZ8NaW-WhcG9jFoN1tGbvTS585jtQBlKmmaw5dIK6H_HUPYujI7y7Ld5G6F-un9FFpTgB6ML21gJ2kLozw=") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "AnonyumAz")
    DB_URI = getenv("DATABASE_URL", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    DB_URI = DB_URI.replace("postgres", "postgres://wdjbvpct:9YeKCuNENv5nctF6LEbeynnPpsoGCYCm@tiny.db.elephantsql.com/wdjbvpct")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "--1001737573985")
    GBAN_LOGS = getenv("GBAN_LOGS", "--1001737573985")
    SYS_ADMIN = getenv("SYS_ADMIN", "5134595693")
    DEV_USERS = getenv("DEV_USERS", "5134595693")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "TheUpdatesChannel")
    SUPPORT = getenv("SUPPORT", "TheSupportChat")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
