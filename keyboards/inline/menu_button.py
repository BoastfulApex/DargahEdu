from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from backend.models import *


async def language_keyboard():
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text="🇺🇿 O'zbek tili(Lotin)")
    key2 = KeyboardButton(text="🇺🇿 Ўзбек тили(Кирил)")
    keyboard.add(key1, key2)
    keyboard.resize_keyboard = True
    return keyboard


async def user_menu(lang):
    texts = []
    if lang == "lat":
        texts = ["Oila kursi haqida", "Status", "Fikr qoldirish"]
    elif lang == "kril":
        texts = ["Оила курси ҳақида", "Статус", "Фикр қолдириш"]

    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"📚 {texts[0]}")
    key3 = KeyboardButton(text=f"✍️ {texts[2]}")
    # keyboard.add(key1)
    keyboard.add(key1, key3)
    keyboard.resize_keyboard = True
    keyboard.one_time_keyboard = True
    return keyboard

async def phone_keyboard(lang):
    texts = []
    if lang == "lat":
        texts = ["Raqamni ulashish", "Ortga"]
    elif lang == "kril":
        texts = ["Рақамни улашиш", "Ортга"]
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"📞 {texts[0]}", request_contact=True)
    key2 = KeyboardButton(text=f"⬅️️ {texts[1]}")
    keyboard.add(key1)
    keyboard.add(key2)
    keyboard.resize_keyboard = True
    return keyboard

async def back_keyboard(lang):
    texts = []
    if lang == "lat":
        texts = ["Ortga"]
    elif lang == "kril":
        texts = ["Ортга"]
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"⬅️️ {texts[0]}")
    keyboard.add(key1)
    keyboard.resize_keyboard = True
    return keyboard


async def cource_buy_keyboard(lang):
    texts = []
    if lang == "lat":
        texts = ["Ortga", "Sotib olish"]
    elif lang == "kril":
        texts = ["Ортга", "Сотиб олиш"]
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"⬅️️ {texts[0]}")
    key2 = KeyboardButton(text=f"🛒 {texts[1]}")
    keyboard.add(key1, key2)
    keyboard.resize_keyboard = True
    return keyboard


async def order_type_keyboard(lang):
    texts = []
    if lang == "lat":
        texts = ["Ortga", "Bir martada to'lov", "Bo'lib to'lash"]
    elif lang == "kril":
        texts = ["Ортга", "Бир мартада тўлов", "Бўлиб тўлаш"]
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"⬅️️ {texts[0]}")
    key2 = KeyboardButton(text=f"❇️ {texts[1]}")
    key3 = KeyboardButton(text=f"🔂 {texts[2]}")
    keyboard.add(key3, key2)
    keyboard.add(key1)
    keyboard.resize_keyboard = True
    return keyboard


async def cource_keyboard(lang):
    texts = []
    cources = Cource.objects.all()
    texts = []
    size = len(cources)
    keyboard = ReplyKeyboardMarkup(row_width=2)
    for i in cources:
        if lang == "lat":
            keyboard.insert(KeyboardButton(text=f"{i.name_lat}"))
        elif lang == "kril":
            keyboard.insert(KeyboardButton(text=f"{i.name_kril}"))
    if lang == "lat":
        texts = ["Asosiy menyu", "Ortga"]
    elif lang == "kril":
        texts = ["Асосий меню", "Ортга"]
    home_key = KeyboardButton(f"⬅️️ {texts[1]}")
    keyboard.add(home_key)  
    keyboard.resize_keyboard = True
    return keyboard


async def pay_method(lang):
    texts = []
    print(lang)
    if lang == "lat":
        texts = ["Click", "Payme", "Ortga"]
    elif lang == "kril":
        texts = ["Click", "Payme", "Ортга"]
    keyboard = ReplyKeyboardMarkup()
    print(texts)
    key1 = KeyboardButton(text=f"🔵 {texts[0]}")
    key2 = KeyboardButton(text=f"🟢 {texts[1]}")
    key3 = KeyboardButton(text=f"⬅️️ {texts[2]}")
    keyboard.add(key1, key2)
    keyboard.add(key3)
    keyboard.resize_keyboard = True
    return keyboard