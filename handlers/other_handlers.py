from create_dp import dp
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


@dp.message()
async def process_no_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer(text=LEXICON_RU['no_echo'])
