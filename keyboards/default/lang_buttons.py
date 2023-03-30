from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove




lang_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oʻz"),
            KeyboardButton(text="Рус")
        ]
    ],
    resize_keyboard=True
)


async def create_main_buttons(lang: str):
    text = {
        'uz': {
        'direction': "Yoʻnalishlar",
        'regestr': "Roʻyxatdan oʻtish",
        'social': "Ijtimoiy tarmoqlar manzillari",
        'address': "Joy manzili",
        'other': "Qo‘shimcha savollar uchun"
        },
        'ru': {
        'direction': "Направления",
        'regestr': "Пройти регистрацию",
        'social': "Адреса социальных сетей",
        'address': "Адрес местонахождения",
        'other': "Для дополнительные вопросы"
        }
    }
    return ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text=text[lang]['direction']),
                KeyboardButton(text=text[lang]['regestr'])
            ],
            [
                KeyboardButton(text=text[lang]['social']),
                KeyboardButton(text=text[lang]['address'])
            ],
            [
                KeyboardButton(text=text[lang]['other'])
            ]
        ],
        resize_keyboard=True
        )


async def create_lesson_type_button(lang: str):
    text = {
        'on': {
        'uz': 'Online',
        'ru': 'Онлайн'
        },
        'off': {
        'uz': 'Offline',
        'ru': 'Оффлайн'
        }
    }
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text= text['on'][lang]),
                KeyboardButton(text= text['off'][lang]),
            ]
        ],
        resize_keyboard=True
        )


remove_keyboard = ReplyKeyboardRemove(selective=False)