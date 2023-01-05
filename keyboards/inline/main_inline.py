from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from backend.models import *
from utils.db_api.database import *

async def test_cource(lang):
    texts = []
    cource = Cource.objects.all()[0]
    if lang == "lat":
        texts = ["Bepul darslar bilan tanish"]
    elif lang == "kril":
        texts = ["Бепул дарслар билан таниш"]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"{texts[0]}", url=f"{cource.test_channel}")],
        ]
    )
    return markup
