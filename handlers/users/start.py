from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text

import asyncio

from keyboards.default.lang_buttons import lang_buttons, create_main_buttons 

from states.reg_form import LangForm
from loader import dp, db


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    text_uz = f"Assalomu alaykum, «Ozodaxon» dizaynerlik kursiga xush kelibsiz!\n"
    text_ru = f"Здравствуйте, добро пожаловать в дизайнерские курсы «Ozodaxon»!\n"
    
    lang_text = "Tilni tanlang: / Выберите язык:"
    db.add_user(message.from_user.id, message.from_user.full_name, "uz")

    lang = db.select_lang(message.from_user.id)
    if lang == "uz":
        text = text_uz + lang_text
    else:
        text = text_ru + lang_text


    await message.answer(text, reply_markup=lang_buttons)
    await LangForm.language.set()
    









@dp.message_handler(Text(equals=['Oʻz','Рус']),state=LangForm.language)
async def choose_language(message: types.Message, state: FSMContext):
    
    db.add_user(message.from_user.id, message.from_user.full_name, 'uz')
    lang = message.text

    text_uz = "Ozodaxon» dizaynerlik kursi haqida batafsil maʼlumot olishni yoki roʻyxatdan " \
                        "oʻtishni xohlasangiz kerakli tugmani bosing!"
    text_ru = "Если хотите узнать полную информацию о дизайнерских курсах «Ozodaxon» или пройти регистрацию, нажмите соответствующую кнопку!"
    text_en = "If you want to get full information about «Ozodaxon» design courses or register, click the corresponding button!"

    if lang == "Oʻz":
        language = "uz"
        text = text_uz
    elif lang == "Рус":
        language = "ru"
        text = text_ru
    else:
        language = "en"
        text = text_en
    db.update_lang(message.from_user.id, language)

    
    await message.answer(text,
                         reply_markup= await create_main_buttons(language))
    await state.finish()