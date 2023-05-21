from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon import LEXICON_RU

# кнопка для начала заполнения своей анкеты
start_button: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['set_up_poll'], 
                                                          callback_data='start_poll')
# клавиатура из кнопок, которые указаны выше
keyboard_start_poll: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[start_button]])
