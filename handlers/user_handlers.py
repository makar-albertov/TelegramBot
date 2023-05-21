from aiogram.types import Message
from aiogram.filters import Command
#импорты файлов из проекта
from lexicon.lexicon import LEXICON_COMMANDS
from create_dp import dp
from keyboards.start_user_poll import keyboard_start_poll


@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_COMMANDS['/start'],
                         reply_markup=keyboard_start_poll)


@dp.message(Command(commands='help'))
async def precess_help_command(message: Message):
    await message.answer(text=LEXICON_COMMANDS['/help'])
