import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
GROUPS_ID = str(os.getenv("GROUPS_ID")).split(" ")
DATABASE = str(os.getenv("DATABASE"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
ADMIN = str(os.getenv("ADMIN")).split(" ")
CLICK_SERVICE_ID = str(os.getenv("CLICK_SERVICE_ID"))
CLICK_MERCHANT_ID = str(os.getenv("CLICK_MERCHANT_ID"))
CLICK_SECRET_KEY = str(os.getenv("CLICK_SECRET_KEY"))
CLICK_MERCHANT_USER_ID = str(os.getenv("CLICK_MERCHANT_USER_ID"))

PAYME_MERCHANT_ID = str(os.getenv("PAYME_MERCHANT_ID"))
PAYME_SECRET_KEY = str(os.getenv("PAYME_SECRET_KEY"))


SLEEP_TIME = .3

ip = str(os.getenv("ip"))

