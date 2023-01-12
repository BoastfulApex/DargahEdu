import datetime
import hashlib
from tokenize import group
from data import config
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from keyboards.inline.menu_button import *
from keyboards.inline.main_inline import *
from utils.db_api.database import *
from django.core.files.base import ContentFile
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle, ChosenInlineResult
from aiogram.dispatcher.filters.builtin import CommandStart
import random
import requests
import re


def isValid(s):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)


def generateOTP():
    return random.randint(111111, 999999)


username = "zoneagency"
password = "j2e4AEFs84"

def send_sms(otp, phone):
    username = 'foodline'
    password = 'JvYkp44)-J&9'
    sms_data = {
        "messages":[{"recipient":f"{phone}","message-id":"abc000000003","sms":{"originator": "3700","content": {"text": f"Sizning Dargoh o'quv platformasida ro'yxatdan o'tish kodingiz: {otp}"}}}]}
    url = "http://91.204.239.44/broker-api/send"
    res = requests.post(url=url, headers={}, auth=(username, password), json=sms_data)


# @dp.message_handler(lambda message: message.text in ["🏠 Asosiy menyu", "🏠 Main menu", "🏠 Главное меню"], state='*')
# async def go_home(message: types.Message, state: FSMContext):
#     lang = await get_lang(message.from_user.id)
#     markup = await user_menu(lang)
#     if lang == "lat":
#         await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
#     elif lang == "ru":
#         await message.answer("Добро пожаловать в наш бот. Выберите нужный раздел👇", reply_markup=markup)
#     elif lang == "en":
#         await message.answer("Welcome to our bot. Please select the desired section 👇", reply_markup=markup)
#     await state.set_state("get_command")
 

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    args = message.get_args()
    if isValid(args):
        user = await get_user_by_phone(args)
        lang = user.lang
        cource = await get_cource_last()
        markup = await user_menu("lat")
        url = await bot.create_chat_invite_link(chat_id=cource.channel, member_limit=1)
        await message.answer(f"✔️ Buyurtma muvaffaqiyatli amalga oshirildi. \nKanaldan foydalanish uchun link:\n{url.invite_link} \nIltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        await state.set_state("get_command")
    else:
        user = await get_user(message.from_id)
        if user is not None:
            lang = user.lang
            if user.phone:
                markup = await user_menu(lang)
                if lang == "lat":
                    await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
                elif lang == "kril":
                    await message.answer("Ботимизга хуш келибсиз. Илтимос керакли бўлимни танланг 👇", reply_markup=markup)
                await state.set_state("get_command")
            else:
                markup = await phone_keyboard(lang)
                if lang == "lat":
                    await message.answer("Telefon raqamingizni ulashing, yoki <b>998YYxxxxxxx</b> tarzida jo'nating", reply_markup=markup)
                if lang == "kril":
                    await message.answer("Телефон рақамингизни жўнатинг, ёки <b>998YYxxxxxxx</b> тарзида жўнатинг", reply_markup=markup)
                await state.set_state('get_phone')    
        else:
            markup = await language_keyboard()
            await message.answer("Assalomu alaykum DargahEdu Botiga xush kelibsiz. Iltimos kerakli alifboni tanlang", reply_markup=markup)
            await state.set_state('get_lang')


@dp.message_handler(state="get_lang")
async def get_language(message: types.Message, state: FSMContext):
    if message.text == "🇺🇿 O'zbek tili(Lotin)":
        user = await add_user(user_id=message.from_user.id, lang="lat")
        markup = await phone_keyboard(user.lang)
        await message.answer("Telefon raqamingizni ulashing, yoki <b>998YYxxxxxxx</b> tarzida jo'nating", reply_markup=markup)
        await state.set_state('get_phone')
    if message.text == "🇺🇿 Ўзбек тили(Кирил)":
        user = await add_user(user_id=message.from_user.id, lang="kril")
        markup = await phone_keyboard(user.lang)
        await message.answer("Телефон рақамингизни жўнатинг, ёки <b>998YYxxxxxxx</b> тарзида жўнатинг", reply_markup=markup)
        await state.set_state('get_phone')


@dp.message_handler(lambda message: message.text in ["⬅️️ Ortga", "⬅️️ Ортга"], state="get_phone")
async def get_phone(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    markup = await language_keyboard()
    await message.answer("Assalomu alaykum DargahEdu Botiga xush kelibsiz. Iltimos siz uchun qulay bo'lgan kiritish usulini tanlang", reply_markup=markup)
    await state.set_state('get_lang')


@dp.message_handler(content_types=types.ContentTypes.TEXT, state="get_phone")
async def get_phone(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if isValid(message.text):
        phone = message.text
        user = await get_user(message.from_user.id)
        user.new_phone = phone
        otp = generateOTP()
        user.otp = otp
        user.save()
        send_sms(phone=phone, otp=otp)
        lang = await get_lang(message.from_user.id)
        keyboard = await back_keyboard(lang)
        if lang == "lat":
            await message.answer(text=f"<b>{user.new_phone}</b> raqamiga yuborilgan tasdiqlash kodini kiriting", parse_mode='HTML', reply_markup=keyboard)
        if lang == "kril":
            await message.answer(text=f"<b>{user.new_phone}</b> рақамига юборилган тасдиқлаш кодини киритинг.", parse_mode='HTML', reply_markup=keyboard)
        await state.set_state("get_otp")
    else:
        markup = await phone_keyboard(lang)
        if lang == "lat":
            await message.answer("Telefon raqamingizni ulashing, yoki <b>998YYxxxxxxx</b> tarzida jo'nating", reply_markup=markup)
        if lang == "kril":
            await message.answer("Телефон рақамингизни жўнатинг, ёки <b>998YYxxxxxxx</b> тарзида жўнатинг", reply_markup=markup)
        await state.set_state('get_phone')    
        


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state="get_phone")
async def get_phone(message: types.Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number[0:]
        user = await get_user(message.from_user.id)
        user.new_phone = phone
        otp = generateOTP()
        user.otp = otp
        user.save()
        send_sms(phone=phone, otp=otp)
        lang = await get_lang(message.from_user.id)
        keyboard = await back_keyboard(lang)
        if lang == "lat":
            await message.answer(text=f"<b>{user.new_phone}</b> raqamiga yuborilgan tasdiqlash kodini kiriting", parse_mode='HTML', reply_markup=keyboard)
        if lang == "kril":
            await message.answer(text=f"<b>{user.new_phone}</b> рақамига юборилган тасдиқлаш кодини киритинг.", parse_mode='HTML', reply_markup=keyboard)
        await state.set_state("get_otp")


@dp.message_handler(lambda message: message.text in ["⬅️️ Ortga", "⬅️️ Ортга"], state="get_otp")
async def get_back_otp(message: types.Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    lang = user.lang
    markup = await phone_keyboard(lang)
    if lang == "lat":
        await message.answer("Telefon raqamingizni jo'nating", reply_markup=markup)
    elif lang == "kril":
        await message.answer("Телефон рақамингизни жўнатинг", reply_markup=markup)
    await state.set_state("get_phone")            

    
@dp.message_handler(content_types=types.ContentTypes.TEXT, state="get_otp")
async def get_phone(message: types.Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    lang = user.lang
    if message.text == user.otp:
        user.phone = user.new_phone
        user.save()
        markup = await user_menu(lang)
        if lang == "lat":
            await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "kril":
            await message.answer("Ботимизга хуш келибсиз. Илтимос керакли бўлимни танланг 👇", reply_markup=markup)
        await state.set_state("get_command")
    else:
        lang = await get_lang(message.from_user.id)
        markup = await back_keyboard(lang)
        if lang == "lat":
            await message.answer("⚠️ Yuborilgan tasdiqlash kodi xato. Qayta urinib ko'ring", reply_markup=markup)
        elif lang == "kril":
            await message.answer("⚠️ Юборилган тасдиқлаш коди хато. Қайта уриниб кўринг", reply_markup=markup)
        await state.set_state("get_otp")
        

@dp.message_handler(lambda message: message.text in ["📚 Oila kursi haqida", "📚 Оила курси ҳақида", "✍️ Fikr qoldirish", "✍️ Фикр қолдириш"], state="get_command")
async def get_user_command(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    command = message.text
    message_id = int(message.message_id) + 1
    if command in ["📚 Oila kursi haqida", "📚 Оила курси ҳақида"]:
        course = await get_cource_by_name("Oila kursi")
        if course is not None:
            await state.update_data(cource_id=course.id)
            markup = await cource_buy_keyboard(lang)
            await message.answer(text='.', reply_markup=markup)
            await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
            test_keyboard = await test_cource(lang)
            if lang == "lat":
                await message.answer(text=f"Kurs Nomi{course.name_lat}\n\nKurs narxi: {course.price}\n\n{course.description_lat}\n\n", reply_markup=test_keyboard)
            if lang == "kril":
                await message.answer(text=f"Курс Номи:   {course.name_kril}\n\nКурс нархи: {course.price}\n\n{course.description_kril}\n\n", reply_markup=test_keyboard)
            await state.set_state("buy_cource")         
    if message.text in ["✍️ Fikr qoldirish", "✍️ Фикр қолдириш"]:
        markup = await back_keyboard(lang)
        if lang == "lat":
            await message.answer(text=f"Fikrlaringizni qoldiring ✍️", reply_markup=markup)
        if lang == "kril":
            await message.answer(text=f"Фикрларингизни қолдиринг ✍️", reply_markup=markup)
        await state.set_state("get_feedback")

@dp.message_handler(state="get_feedback")
async def get_feedback_message(message: types.Message, state:FSMContext):
    if "⬅️️️" in message.text:
        lang = await get_lang(message.from_user.id)
        markup = await user_menu(lang)
        if lang == "lat":
            await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "kril":
            await message.answer("Ботимизга хуш келибсиз. Илтимос керакли бўлимни танланг 👇", reply_markup=markup)
        await state.set_state("get_command")
    else:
        await message.forward(chat_id=-882055933)
        lang = await get_lang(message.from_user.id)
        markup = await user_menu(lang)
        if lang == "lat":
            await message.answer("Fikr-mulohazangiz uchun tashakkur!", reply_markup=markup)
        elif lang == "kril":
            await message.answer("Фикр-мулоҳазангиз учун ташаккур!", reply_markup=markup)
        await state.set_state("get_command")


@dp.message_handler(content_types=types.ContentTypes.TEXT, state="buy_cource")
async def get_course(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    user = await get_user(message.from_user.id)
    if "⬅️️" in message.text:
        markup = await user_menu(lang)
        if lang == "lat":
            await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "kril":
            await message.answer("Ботимизга хуш келибсиз. Илтимос керакли бўлимни танланг 👇", reply_markup=markup)
        await state.set_state("get_command")
    if message.text in ["🛒 Сотиб олиш", "🛒 Sotib olish"]:
        markup = await order_type_keyboard(lang)
        if lang == "lat":
            await message.answer("💸 To'lov turini tanlang 👇", reply_markup=markup)
        elif lang == "kril":
            await message.answer("💸 Тўлов турини танланг 👇", reply_markup=markup)
        await state.set_state("pay_type")


@dp.message_handler(content_types=types.ContentTypes.TEXT, state="pay_type")
async def get_course(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    user = await get_user(message.from_user.id)
    if message.text in ["⬅️️ Ortga", "⬅️️ Ортга"]:
        data = await state.get_data()
        cource_id  = data["cource_id"]
        course = await get_cource(cource_id)
        markup = await cource_buy_keyboard(lang)
        if lang == "lat":
            await message.answer(text=f"Kurs Nomi{course.name_lat}\n\nKurs narxi: {course.price}\n\n{course.description_lat}\n\nBepul tanishuv: {course.test_channel}", reply_markup=markup)
        if lang == "kril":
            await message.answer(text=f"Курс Номи:   {course.name_kril}\n\nКурс нархи: {course.price}\n\n{course.description_kril}\n\nБепул танишув: {course.test_channel}", reply_markup=markup)
        await state.set_state("buy_cource")         
    if message.text in ["🔂 Бўлиб тўлаш", "🔂 Bo'lib to'lash"]:
        markup = await order_type_keyboard(lang)
        if lang == "lat":
            await message.answer("ℹ️ Ushbu qism ustida ishlar olib borilmoqda 👇", reply_markup=markup)
        elif lang == "kril":
            await message.answer("ℹ️ Ушбу қисм устида ишлар олиб борилмоқда 👇", reply_markup=markup)
    if message.text in ["❇️ Бир мартада тўлов", "❇️ Bir martada to'lov"]:
        markup = await pay_method(lang)
        if lang == "lat":
            await message.answer("To'lov usulini tanlang 👇", reply_markup=markup)
        elif lang == "kril":
            await message.answer("Тўлов усулини танланг 👇", reply_markup=markup)
        await state.set_state("get_payment_method")


@dp.message_handler(content_types=types.ContentTypes.TEXT, state="get_payment_method")
async def get_course(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    user = await get_user(message.from_user.id)
    if message.text in ["⬅️️ Ortga", "⬅️️ Ортга"]:
        markup = await order_type_keyboard(lang)
        if lang == "lat":
            await message.answer("💸 To'lov turini tanlang 👇", reply_markup=markup)
        elif lang == "kril":
            await message.answer("💸 Тўлов турини танланг 👇", reply_markup=markup)
        await state.set_state("pay_type")
    elif message.text in ["🔵 Click", "🟢 Payme"]:
        prices = []
        markup = await back_keyboard(lang)
        await message.answer(text='.', reply_markup=markup)
        data = await state.get_data()
        cource_id  = data["cource_id"]
        course = await get_cource(cource_id)
        message_id = message.message_id + 2
        await state.update_data(message_id=message_id)
        if message.text == "🔵 Click":
            photo = 'https://click.uz/click/images/clickog.png'
            token = '398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065'
        elif message.text == "🟢 Payme":
            photo = "https://cdn.paycom.uz/documentation_assets/payme_01.png"
            token = '371317599:TEST:1672069604730'
        texts = []
        if lang == "lat":
            texts = ["Kurs uchun to'lov"]
            prices.append(
                types.LabeledPrice(label=f"{course.name_lat}", amount=int(course.price) * 100))
        if lang == "kril":
            texts = ["Курс учун тўлов"]
            prices.append(
                types.LabeledPrice(label=f"{course.name_kril}", amount=int(course.price) * 100))
        await bot.send_invoice(chat_id=message.from_user.id, title=f'Dargah Edu',
                               description=f'{texts[0]}',
                               provider_token=token,
                               currency='UZS',
                               photo_url=photo,
                               photo_height=512,  # !=0/None or picture won't be shown
                               photo_width=512,
                               photo_size=512,
                               prices=prices,
                               start_parameter='hz-wto-tut',
                               payload="Payload",
                               )
        await state.set_state("payment")  
   

@dp.message_handler(state="payment")
async def get_payment(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if "⬅️" in message.text:
        data = await state.get_data()
        message_id = data['message_id']
        await bot.delete_message(message_id=message_id, chat_id=message.from_id)
        data = await state.get_data()
        cource_id  = data["cource_id"]
        cource = await get_cource(cource_id)
        markup = await pay_method(lang)
        if lang == "lat":
            await message.answer("To'lov usulini tanlang 👇", reply_markup=markup)
        elif lang == "kril":
            await message.answer("Тўлов усулини танланг 👇", reply_markup=markup)
        await state.set_state("get_payment_method")
                

@dp.pre_checkout_query_handler(lambda query: True, state='payment')
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=types.ContentTypes.SUCCESSFUL_PAYMENT, state="payment")
async def got_payment(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_id)
    markup = await user_menu(lang)
    data = await state.get_data()
    message_id = data['message_id']
    await bot.delete_message(message_id=message_id, chat_id=message.from_id)
    data = await state.get_data()
    cource_id  = data["cource_id"]
    cource = await get_cource(cource_id)
    url = await bot.create_chat_invite_link(chat_id=cource.channel, member_limit=1)

    if lang == "lat":
        await message.answer(f"✔️ Buyurtma muvaffaqiyatli amalga oshirildi. \nKanaldan foydalanish uchun link:\n{url.invite_link} \nIltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
    elif lang == "kril":
        await message.answer(f"✔️ Буюртма муваффақиятли амалга оширилди. \нКаналдан фойдаланиш учун линк:\н{url.invite_link} \нИлтимос керакли бўлимни танланг 👇", reply_markup=markup)
    await state.set_state("get_command")
