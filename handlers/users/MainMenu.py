import asyncio
from aiogram import types
from aiogram.dispatcher.filters.builtin import Text

from aiogram.dispatcher import FSMContext


from keyboards.default.lang_buttons import lang_buttons, create_lesson_type_button, create_main_buttons

from states.reg_form import RegForm
from loader import dp, bot, db

from data.config import ADMINS, OWNER_ID



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
        text_cancel = "Amallar to'xtatildi! Ma'lumotlar tozalandi!"
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




@dp.message_handler(Text(equals=["Yoʻnalishlar", "Направления"]), state="*")
async def show_directions(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    db.add_user(message.from_user.id, message.from_user.full_name, 'uz')
    full_text_uz = "<b>Dizaynerlik kursi yo’nalishlari:</b>\n\n"\
        "<b>🫰Dizaynerlik kursi</b>: 10 yoshdan boshlab 35 yoshgacha bo’lgan qiz va ayollar uchun.\n\n"\
        "⏭ 3 oydan 6 oygacha.\n\n"\
        "<b>🫰Institutga tayyorlov kursi</b>: Libos dizayn fakultetlarining ijodiy imtihoniga bilet asosida tayyorlanadi.\n\n"\
        "⏭ Kamida 6 oy\n\n"\
        "<b>🫰 Chizmatasvir</b>: ijodiy imtihonlarda tushadigan natyurmort va haykal chizishga tayyorlov. \n\n"\
        "⏭ Kamida 6 oy\n\n"\
        "<b>🫰Havaskor rassom</b>: Rassomlikka qiziquvchilar uchun har-xil texnikalarni o’rganiladi.\n\n"\
        "⏭ 3 oydan 6 oygacha\n\n"\
        "<b>🫰 Digital Fashion illustratsiya</b>:\n\n"\
        "Zamonaviy kasblardan biri iPad yordamida har xil dasturlar orqali eskizlarni elektron chizishni o’rganish.\n\n"\
        "⏭ 2 oy"
    
    full_text_ru = "Направлении дизайнерских курсов:\n\n"\
                "🫰Дизайнерские курсы: начиная от 10 лет до 35 лет для женщин и девушек.\n\n"\
                "⏭ От 3 до 6 месяцев.\n\n"\
                "🫰Подготовительные курсы для института: Подготовка к творческому экзамену по билетам для факультета дизайн одежды.\n\n"\
                "⏭ Минимум 6 месяцев.\n\n"\
                "🫰Рисунок: Подготовка к творческому экзамену по билетам натюрморт и рисование статуи.\n\n"\
                "⏭ Минимум 6 месяцев \n\n"\
                "🫰 Художник-любитель: изучение различных техник для интересующихся живописью.\n\n"\
                "⏭ от 3 до 6 месяцев. \n\n"\
                "🫰 Цифровая модная иллюстрация: одной из современных профессий является обучение электронному "\
                "скетчингу в различных программах с помощью iPad.\n\n"\
                "⏭ 2 месяца."""
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        full_text = full_text_uz
    else:
        full_text = full_text_ru
    await message.answer(full_text)







@dp.message_handler(Text(equals=["Ijtimoiy tarmoqlar manzillari", "Адреса социальных сетей"]))
async def show_socials(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    db.add_user(message.from_user.id, message.from_user.full_name, 'uz')
    text_uz = "<b>Men va mening ishtimoiy tarmoqlardagi manzillarim quyidagilar:</b> \n\n"\
            "<b>Ozodaxon dizayner</b>\n"\
            "<a href=\"https://instagram.com/ozodaxon.dizayner?igshid=YmMyMTA2M2Y\">Instagram</a>\n\n"\
            "<b>«Ozodaxon» dizaynerlik kursi</b>\n"\
            "<a href=\"https://t.me/dizaynerlik_kursi1\">Telegram</a> | "\
            "<a href=\"https://instagram.com/dizaynerlik.kursi?igshid=Mzc1MmZhNjY\">Instagram</a> | "\
            "<a href=\"https://www.tiktok.com/@ozodaxon.dizayner?_t=8b4db19jidN\">Tiktok</a>"
    
    text_ru = "<b>Я и мои адреса в социальных сетях:</b> \n\n"\
            "<b>«Ozodaxon» дизайнер</b>\n"\
            "<a href=\"https://instagram.com/ozodaxon.dizayner?igshid=YmMyMTA2M2Y\">Instagram</a>\n\n"\
            "<b>Курс дизайна \"Ozodaxon\"</b>\n"\
            "<a href=\"https://t.me/dizaynerlik_kursi1\">Telegram</a> | "\
            "<a href=\"https://instagram.com/dizaynerlik.kursi?igshid=Mzc1MmZhNjY\">Instagram</a> | "\
            "<a href=\"https://www.tiktok.com/@ozodaxon.dizayner?_t=8b4db19jidN\">Tiktok</a>"
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
    else:
        text = text_ru
    await message.answer(text, disable_web_page_preview=True)




@dp.message_handler(Text(equals=["Joy manzili","Адрес местонахождения"]))
async def show_address(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    db.add_user(message.from_user.id, message.from_user.full_name, 'uz')
    text_uz = "<b>☎️ Murojaat uchun: </b>\n"\
        "📞 +998998721728 \n\n"\
        "<b>⛳️ Manzil:</b> Toshkent shahar, Chilonzor \"Торговый центр\".\n\n"\
        "<b>🎯 Moʻljal</b>: Yuri Gagarin haykali yonida joylashgan o’quv markaz.\n\n"\
        "<b>🚌 Yoʻnalishdagi avtobuslar:</b>\n"\
        "2 | 80 | 84 | 94 | 98 | 103 | 135"
    
    text_ru = "<b>☎️ Для справки: </b>\n"\
        "📞 +998998721728 \n\n"\
        "<b>⛳️ Адрес:</b> город Ташкент, Чилонзор, Торговый центр.\".\n\n"\
        "<b>🎯 Ориентир:</b> образовательный центр, расположенный рядом со статуей Юрия Гагарина.\n\n"\
        "<b>🚌 Автобусы по направлению:</b>\n"\
        "2 | 80 | 84 | 94 | 98 | 103 | 135"
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
    else:
        text = text_ru
    await message.answer(text)



@dp.message_handler(Text(equals=["Qo‘shimcha savollar uchun", "Для дополнительные вопросы"]))
async def show_address(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    db.add_user(message.from_user.id, message.from_user.full_name, 'uz')
    text_uz = "<b>Qo‘shimcha savollaringiz bo'lsa admin bilan quyidagi manzillar bilan bog‘laning:</b>\n\n"\
        "📞 +998998721728 \n\n"\
        "📨 @ozodaxon_dizayner"
    
    text_ru = "<b>Если у вас есть дополнительные вопросы, свяжитесь с администратором по следующим адресам:</b>\n\n"\
        "📞 +998998721728 \n\n"\
        "📨 @ozodaxon_dizayner"
    
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
    else:
        text = text_ru
    await message.answer(text)







@dp.message_handler(Text(equals=["Roʻyxatdan oʻtish", "Пройти регистрацию"]))
async def reg_form(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    db.add_user(message.from_user.id, message.from_user.full_name, 'uz')
    text_uz = "«Ozodaxon» dizaynerlik kursida, roʻyxatdan oʻtish uchun quyidagi savollarga javob yozing! \n"\
                "Amalllarni bekor qilish uchun /cancel buyrug‘ini bering !!!\n\n"\
                "> Ismingiz / Familiyangiz / Otangizning ismi"
    text_ru = "Чтобы записаться на курс дизайна «Ozodaxon», ответьте на следующие вопросы!\n"\
                "Чтобы отменить действия, введите команду /cancel !!!\n\n"\
                "> Имя/ Фамилия/ Отчество"
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
    else:
        text = text_ru


    await message.answer(text=text)
    await RegForm.full_name.set()


@dp.message_handler(state=RegForm.full_name)
async def full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    text_uz = "> Yoshingiz nechchida?"
    text_ru = "> Сколько вам лет?"
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
    else:
        text = text_ru
    
    await message.answer(text)
    await RegForm.age.set()



@dp.message_handler(state=RegForm.age)
async def age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    text_uz = "> Qayerdansiz?"
    text_ru = "> Откуда вы?"
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
    else:
        text = text_ru
    await message.answer(text)
    await RegForm.from_where.set()


@dp.message_handler(state=RegForm.from_where)
async def from_where(message: types.Message, state: FSMContext):
    from_where = message.text
    await state.update_data(from_where=from_where)
    
    text_uz = "> Qaysi yoʻnalishni tanladingiz?"
    text_ru = "> Какое направление вы выбрали?"
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
    else:
        text = text_ru
    await message.answer(text)
    await RegForm.course.set()


@dp.message_handler(state=RegForm.course)
async def course(message: types.Message, state: FSMContext):
    course = message.text
    await state.update_data(course=course)
    text_uz = "> Dars turini tanlang:"
    text_ru = "> Выберите тип урока:"
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
        lang = 'uz'
    else:
        text = text_ru
        lang = 'ru'
    await message.answer(text=text, reply_markup= await create_lesson_type_button(lang=lang))
    await RegForm.lesson_type.set()


@dp.message_handler(Text(equals=['Online','Онлайн','Offline','Оффлайн']),state=RegForm.lesson_type)
async def lesson_type(message: types.Message, state: FSMContext):
    lesson_type = message.text
    await state.update_data(lesson_type=lesson_type)
    text_uz = "> Telefon raqamingizni kiriting:"
    text_ru = "> Номер телефона:"
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
    else:
        text = text_ru
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove(selective=False))
    await RegForm.phone_number.set()


@dp.message_handler(state=RegForm.phone_number)
async def phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    text_uz = "> Siz muvaffaqiyatli ro‘yxatdan o‘tdingiz!"
    text_ru = "> Вы успешно зарегистрировались!"
    language = db.select_lang(message.from_user.id)
    if language == 'uz':
        text = text_uz
        lang = 'uz'
    else:
        text = text_ru
        lang = 'ru'
    await message.answer(text=text, reply_markup= await create_main_buttons(lang))
    
    data = await state.get_data()
    await send_to_admin(data)
    await state.finish()





async def send_to_admin(data):
    full_name = data.get("full_name")
    age = data.get("age")
    from_where = data.get("from_where")
    course = data.get("course")
    lesson_type = data.get("lesson_type")
    phone_number = data.get("phone_number")
    full_text = f"Ro'yxatdan o'tgan foydalanuvchi haqida ma'lumotlar:\n\n"\
        f"<b>👤To‘liq ismi</b>: {full_name}\n\n"\
        f"<b>Yoshi</b>: {age}\n\n"\
        f"<b>Manzili</b>: {from_where}\n\n"\
        f"<b>Tanlagan yo‘nalishi</b>: {course}\n\n"\
        f"<b>Tanlagan dars turi</b>: {lesson_type}\n\n"\
        f"<b>Telefon raqami</b>: {phone_number}\n\n"
    await bot.send_message(chat_id=OWNER_ID, text="Yana bir foydalanuvchi ro'yxatdan o'tdi!")
    await bot.send_message(chat_id=OWNER_ID, text=full_text)