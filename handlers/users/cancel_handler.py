from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher import FSMContext
from aiogram import types

import asyncio
from loader import dp, db



from keyboards.default.lang_buttons import create_main_buttons

@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        lang = 'uz'
        text_cancel = "Amallar to'xtatildi! Ma'lumotlar tozalandi!!"
        text_menu = "Ozodaxon» dizaynerlik kursi haqida batafsil maʼlumot olishni yoki roʻyxatdan " \
                        "oʻtishni xohlasangiz kerakli tugmani bosing!"
    else:
        lang = 'ru'
        text_cancel = "Действия остановлены! Данные очищены!"
        text_menu = "Если хотите узнать полную информацию о дизайнерских курсах «Ozodaxon» "\
                        "или пройти регистрацию, нажмите соответствующую кнопку!"
    
    await message.reply(text=text_cancel, reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await message.answer(text=text_menu, reply_markup= await create_main_buttons(lang=lang))